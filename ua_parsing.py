#!interpreter [python3]
# -*- coding: utf-8 -*-

"""
Script for parsing UserAgent strings with an additional column "cnt"
(count). All information of a UserAgent is parsed and written to an 
output Excel table.

Finally, finds the shares of Operative System (OS), browser and device
type among the User Agents and plots relative charts.

It is necessary for the original table to have a first string column
with the user agent string and a second integer column with a count 
value.
"""

__author__ = 'Luca Iacolettig'
__copyright__ = 'Copyright 2022, skitourenguru.ch'
__email__ = 'iacolettig.luca@gmail.com'
__version__ = '1.2'
__license__ = 'GNU GPL v3'

#
# Import modules
#
import pandas as pd

# Read/write Excel xlsx files
import openpyxl     

# UserAgent parser https://github.com/ua-parser/uap-python
from ua_parser import user_agent_parser  

# Another UserAgent parser
# not used https://github.com/selwin/python-user-agents
# from user_agents import parse 

# To create charts
import matplotlib.pyplot as plt

#
# Defining functions
#
def readData(file):
    """Reads from Excel using Pandas
    
    Parameters
    ----------
    file : str
        The file location of the xls(x) spreadsheet

    Returns
    -------
    pd.read_excel(file)
        The read Excel file by Pandas
    """

    return pd.read_excel(file)
    
def saveData(df, outputFileName):
    """Saves the data to an Excel outputFileName
    
    Parameters
    ----------
    df : DataFrame
        The DataFrame that wants to be saved
    outputFileName : str
        The file location of the output xlsx file

    Returns
    -------
    df.to_excel(outputFileName, index=True)
        The Excel file of the DataFrame df
        Keeps the index of the DataFrame
    """

    return df.to_excel(outputFileName, index=True) 

def parseUserAgentStrings(df):
    """Parses the UserAgents to obtain a table with all possible information on them
    
    Parameters
    ----------
    df : DataFrame
        The DataFrame of the UserAgent strings and count value

    Returns
    -------
    final_table
        The DataFrame of all parsed data of the UserAgent
    """

    # Create two dataframes from the input argument
    userAgent = df['userAgent']
    cnt = df['cnt']
    
    # Create empty lists for the results of the following for loop
    ua_parsed = []
    browser_data = []
    os_info = []
    device_info = []

    # Iterate over the userAgent strings
    for ua_string in userAgent:
        ua_parsed.append(
            user_agent_parser.Parse(ua_string)
        )
        browser_data.append(
            user_agent_parser.ParseUserAgent(ua_string)
        )
        os_info.append(
            user_agent_parser.ParseOS(ua_string)
        )
        device_info.append(
            user_agent_parser.ParseDevice(ua_string)
        )

    # Create different dataframes of the parsed data
    ua_parsed = pd.DataFrame(ua_parsed)
    browser_data = pd.DataFrame(browser_data)
    os_info = pd.DataFrame(os_info)
    device_info = pd.DataFrame(device_info)
    
    # Rename columns
    browser_data.rename(columns = {'family':'browser'}, inplace = True)
    os_info.rename(columns = {'family':'OS'}, inplace = True)
    device_info.rename(columns = {'family':'device_type'}, inplace = True)

    # Join all relevant data
    final_table = pd.concat([ua_parsed, browser_data, os_info, device_info, cnt], axis=1)

    # Boolean condition for PCs
    for i in range(len(final_table)):
        osys = final_table.loc[i,'OS']
        final_table.loc[i,'is_pc'] = (osys == 'Mac OS X') | (osys == 'Windows') | (osys == 'Ubuntu') | (osys == 'Linux') | (osys == 'Fedora') | (osys == 'Solaris')

    # Boolean condition for mobile (smartphone + tablet)
    for i in range(len(final_table)):
        final_table.loc[i,'is_mobile'] = not final_table.loc[i,'is_pc'] 

    # Create column pc_or_mobile based on boolean values 
    for i in range(len(final_table)):
        if final_table.loc[i, 'is_pc'] == True:
            final_table.loc[i, 'pc_or_mobile'] = 'pc'
        else:
            final_table.loc[i, 'pc_or_mobile'] = 'mobile'

    # Drop unused columns and rename columns string to user_agent
    final_table.drop(['user_agent', 'os', 'device', 'is_pc', 'is_mobile'], axis=1, inplace=True)
    final_table.rename(columns = {'string':'user_agent'}, inplace = True)
    
    # Return the DataFrame of all parsed data
    return final_table

def deduceOsShares(df):
    """Deduce the OS shares from the data table
    
    Parameters
    ----------
    df : DataFrame
        The DataFrame that wants to be deduced (the one of operative
        systems)

    Returns
    -------
    os_count_res
        The resulting DataFrame of the counted OperativeSystems
        The DataFrame is weighted based on the count column of the
        original UserAgent table
    """

    os = pd.DataFrame(df[['OS', 'cnt']])
    
    os_count = pd.DataFrame(os.groupby(['OS'])['cnt'].sum().reset_index())
    os_count = os_count.sort_values(by='cnt', ascending=False)

    # Create dictionary with Win, iOS, Mac OS X, Android, Linux
    os_dict = {
        "Android" : "Android",
        "iOS" : "iOS",
        "Windows" : "Windows",
        "Mac OS X" : "Mac OS X",
        "Linux" : "Linux",
        "Ubuntu" : "Linux",
        "Fedora" : "Linux"
    }

    # Create a subset of the data based on a condition
    os_count_sel = os_count[os_count['OS'].isin(['Android', 'iOS', 'Windows', 'Mac OS X', 'Linux', 'Ubuntu', 'Fedora'])].reset_index()
    os_count_sel.drop('index', axis=1, inplace=True)
    
    os_count_res = pd.DataFrame(columns=['OS', 'cnt'])
    
    # Iterate over the rows to make all similar OSs one and the same
    # E.g. all Linux distros as Linux
    for i in range(len(os_count_sel)):
        # define variables by accessing os_count_sel
        os = os_count_sel.loc[i, 'OS']
        cnt = os_count_sel.loc[i, 'cnt']
        # determine the group of a certain OS based on the os_dict
        group = os_dict.get(os)

        # Populate the new empty table
        if group in os_count_res['OS']:
            os_count_res.loc[group, 'cnt'] += cnt
        else:
            os_count_res.loc[group, 'cnt'] = cnt

    os_count_res.drop('OS', axis=1, inplace=True)
    
    return os_count_res
 
def deduceBrowserShares(df):
    """Deduce the browser shares from the data table
    
    Parameters
    ----------
    df : DataFrame
        The DataFrame that wants to be deduced (the one of browsers)

    Returns
    -------
    os_count_res
        The resulting DataFrame of the counted browsers
        The DataFrame is weighted based on the count column of the
        original UserAgent table
    """

    browser = pd.DataFrame(df[['browser', 'cnt']])
    
    browser_count = pd.DataFrame(browser.groupby(['browser'])['cnt'].sum().reset_index())
    browser_count = browser_count.sort_values(by='cnt', ascending=False)
    
    # Create dictionary for Firefox, Chrome, Safari, Opera, Edge
    browser_dict = {
        "Chrome" : "Chrome",
        "Chrome Mobile iOS" : "Chrome",
        "Chrome Mobile WebView" : "Chrome",
        "Chromium" : "Chrome",
        "Firefox" : "Firefox",
        "Firefox Mobile" : "Firefox",
        "Firefox iOS" : "Firefox",
        "Safari" : "Safari",
        "Mobile Safari" : "Safari",
        "Mobile Safari UI/WKWebView" : "Safari",
        "Opera" : "Opera",
        "Edge" : "Edge",
        "Edge Mobile" : "Edge"
    }
    
    browser_count_sel = browser_count[browser_count['browser'].isin(['Chrome', 'Chrome Mobile iOS', 'Chrome Mobile WebView', 'Chromium', 'Firefox', 'Firefox Mobile', 'Firefox iOS', 'Safari', 'Mobile Safari', 'Mobile Safari UI/WKWebView', 'Opera', 'Edge', 'Edge Mobile'])].reset_index()
    browser_count_sel.drop('index', axis=1, inplace=True)
    
    # Create empty DataFrame
    browser_count_res = pd.DataFrame(columns=['browser', 'cnt'])

    # Iterate over the rows to make all similar browsers one and the same
    # all Chrome distros as Chrome, etc...
    for i in range(len(browser_count_sel)):
        
        # define variables by accessing os_count_sel
        browser = browser_count_sel.loc[i, 'browser']
        cnt = browser_count_sel.loc[i, 'cnt']
        
        # determine the group of a certain OS based on the os_dict
        group = browser_dict.get(browser)

        # Populate the new empty table
        if group in browser_count_res['browser']:
            browser_count_res.loc[group, 'cnt'] += cnt
        else:
            browser_count_res.loc[group, 'cnt'] = cnt
    
    # Drop empty columns
    browser_count_res.drop('browser', axis=1, inplace=True)
    
    return browser_count_res

def deduceDeviceShares(df):
    """Deduce the device shares from the data table
    
    Parameters
    ----------
    df : DataFrame
        The DataFrame that wants to be deduced (the one of devices)

    Returns
    -------
    os_count_res
        The resulting DataFrame of the counted devices
        The DataFrame is weighted based on the count column of the
        original UserAgent table
    """
    
    # Create different tables for data analysis
    device = pd.DataFrame(df[['pc_or_mobile', 'cnt']])

    # Count occurences in the different tables
    device_count = pd.DataFrame(device.groupby(['pc_or_mobile'])['cnt'].sum().reset_index())
    device_count = device_count.sort_values(by='cnt', ascending=False)
    device_count = device_count.set_index('pc_or_mobile')
    
    return device_count

def plot(df, file):
    """Plots a pie chart based on df and saves it in file
    
    Parameters
    ----------
    df : DataFrame
        The DataFrame that wants to be plotted. It has to have the 
        index represented by words and one column with the numeric data
    file : str
        The file path of the image (png, pdf...) that wants to be 
        exported
    """

    # Plot the data
    ax = df.plot(kind='pie', y='cnt', autopct='%1.0f%%')
    
    # Remove the legend
    ax.get_legend().remove()

    # Remove the y label
    ax.set(ylabel=None)

    # Save the figure to the declared output
    plt.savefig(file, dpi=600)
    
#
# Main script
#

# Define the initial variables 
# File paths of input and output files
inputFileName = 'Unique_UserAgents_sample.xlsx'
outputFileName = 'Unique_UserAgents_parsed.xlsx'
osFile = 'OS_count.xlsx'
browserFile = 'browse_count.xlsx'
deviceFile = 'device_count.xlsx'
plotOsFileName = 'piechart_os.png'
plotBrowserFileName = 'piechart_browser.png'
plotDeviceFileName = 'piechart_device.png'

# Read, parse and save the data
print("Parsing data, please wait...")
data = readData(inputFileName)
data = parseUserAgentStrings(data)
saveData(data, outputFileName)

# Deduce the shares of OS, browser and device 
print("""I have saved the output table of the parsed data.
Continuing with OS, browser and device shares...""")
osShares = deduceOsShares(data)
browserShares = deduceBrowserShares(data)
deviceShares = deduceDeviceShares(data)

# Save the tables of the OS, browser and device shares 
print("Analysed data, now saving the relative OS, browser and device shares tables.")
saveData(osShares, osFile)
saveData(browserShares, browserFile)
saveData(deviceShares, deviceFile)

# Plot the data od the OS, browser and device shares 
print("The tables are exported, now plotting and saving the data...")
plot(osShares, plotOsFileName)
plot(browserShares, plotBrowserFileName)
plot(deviceShares, plotDeviceFileName)

print("Done!")
