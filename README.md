# User-agent-parser
Python script that parses an Excel table of UserAgents together with their count number to produce statistics on the data.

## Technology used
### Interpreter
Python 3.9.7

### Python libraries
* pandas 
* openpyxl
* [ua_parser](https://github.com/ua-parser/uap-python)
* matplotlib.pyplot

## Usage example
1. Create a folder with [ua_parsing.py](https://github.com/lucalevi/User-agent-parser/blob/main/ua_parsing.py) and your Excel table of UserAgents and count number. We will use [Unique_UserAgents_sample.xlsx](https://github.com/lucalevi/User-agent-parser/blob/main/Unique_UserAgents_sample.xlsx).
2. Open a terminal in the folder and run
```
python3 ua_parsing.py
```
3. Let the program run.

As output, you will have an Excel table of the parsed UserAgent data ([here](https://github.com/lucalevi/User-agent-parser/blob/main/Unique_UserAgents_parsed.xlsx) an example) 

Afterwards, some statistics are calculated to verify the shares in the data among the Operative Systems, browsers and device type used. The script then outputs three Excel tables, one for each share (OS, browser, device type) and plots the data graphically with pie charts. You find sample outputs in the repo.


## What's in this repo
The main script is ua_parsing.py.
It is a Python3 script that parses the sample Excel table "Unique_UserAgents_sample.xlsx" thanks to the module [ua_parser](https://github.com/ua-parser/uap-python).



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
