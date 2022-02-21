# User-agent-parser
Python script that parses an Excel table of UserAgents together with their count number to produce statistics on the data.

## Technology
### Interpreter
Python 3.9.7

### Python libraries
Install the following libraries before running the script:
* pandas 
* openpyxl
* [ua_parser](https://github.com/ua-parser/uap-python)
* matplotlib.pyplot

In a terminal, use the follwing command to install the libraries. Change "name" to the wished library
```
$ pip install name
```

## Usage example
1. Create a folder with [ua_parsing.py](https://github.com/lucalevi/User-agent-parser/blob/main/ua_parsing.py) and your Excel table of UserAgents and relative count number (cnt). We will use [Unique_UserAgents_sample.xlsx](https://github.com/lucalevi/User-agent-parser/blob/main/Unique_UserAgents_sample.xlsx).
2. In the [script](https://github.com/lucalevi/User-agent-parser/blob/main/ua_parsing.py), adapt the following lines according to your need. Most likely, you will have a different inputFileName.
```python
inputFileName = 'Unique_UserAgents_sample.xlsx'
outputFileName = 'Unique_UserAgents_parsed.xlsx'
osFile = 'OS_count.xlsx'
browserFile = 'browse_count.xlsx'
deviceFile = 'device_count.xlsx'
plotOsFileName = 'piechart_os.png'
plotBrowserFileName = 'piechart_browser.png'
plotDeviceFileName = 'piechart_device.png'
4. Open a terminal in the folder and run
```
3. Open a terminal in the created folder and run:
```
python3 ua_parsing.py
```
5. As output, you will have an Excel table of the parsed UserAgent data ([here](https://github.com/lucalevi/User-agent-parser/blob/main/Unique_UserAgents_parsed.xlsx) an example).
![Parsed UserAgent data](https://github.com/lucalevi/User-agent-parser/blob/main/Unique_UserAgents_parsed.png "Parsed UserAgent data")

6. Afterwards, some statistics are calculated to verify the shares in the data among the Operative Systems, browsers and device type used. 
 * The script outputs three Excel tables, one for each share (OS, browser, device type)
  
 ![Example of output table](https://github.com/lucalevi/User-agent-parser/blob/main/OS_count.png "Example of OS output table")
 * it plots the data graphically with pie charts.
 ![Example of OS share pie chart](https://github.com/lucalevi/User-agent-parser/blob/main/piechart_os.png "Example of OS share pie chart")


## What's in this repo
The main files in this repo are:
* [ua_parsing.py](https://github.com/lucalevi/User-agent-parser/blob/main/ua_parsing.py): the Python script that parses the user agent data.
* [Unique_UserAgents_sample.xlsx](https://github.com/lucalevi/User-agent-parser/blob/main/Unique_UserAgents_sample.xlsx): sample table of unique UserAgents and their relative count number (these are e.g. counts of how many unique UserAgents clicked on a certain web page.)
* [Unique_UserAgents_parsed.xlsx](https://github.com/lucalevi/User-agent-parser/blob/main/Unique_UserAgents_parsed.xlsx): output table of the parsed data. It contains multiple columns with information about Operative System, browser and device type used, together with the count number of the input table.
* [OS_count.xlsx](https://github.com/lucalevi/User-agent-parser/blob/main/OS_count.xlsx), [browse_count.xlsx](https://github.com/lucalevi/User-agent-parser/blob/main/browse_count.xlsx) and [device_count.xlsx](https://github.com/lucalevi/User-agent-parser/blob/main/device_count.xlsx): three sample output tables calculated by the script. They are obtained by a groupby() function.
* [piechart_os.png](https://github.com/lucalevi/User-agent-parser/blob/main/piechart_os.png), [piechart_browser.png](https://github.com/lucalevi/User-agent-parser/blob/main/piechart_browser.png) and [piechart_device.png](https://github.com/lucalevi/User-agent-parser/blob/main/piechart_device.png): the pie charts plotted based on the output tables of the previous point.


### Which OSs, browsers and device types are included in the data analysis?

#### OSs: 
* Windows
* iOS
* Mac
* OS X
* Android
* Linux

#### Browsers: 
* Firefox
* Chrome
* Safari
* Opera
* Edge

#### Device types:
* Computer
* Mobile (smartphones + tablets)


## Release History
* 1.2 
  * The first proper release

## Meta

Author: Luca Iacolettig - iacolettig(dot)luca(at)gmail.com

Distributed under the GNU GPL v3 license. See [LICENSE](..User-agent-parser/LICENSE) for more information.
