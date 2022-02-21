# User-agent-parser
Python script that parses an Excel table of UserAgents together with their count number to produce statistics on the data.

## Usage example



## What's in this repo
The main script is ua_parsing.py.
It is a Python3 script that parses the sample Excel table "Unique_UserAgents_sample.xlsx" thanks to the module [ua_parser](https://github.com/ua-parser/uap-python).

Once parsed all data, an Excel output table is saved (Unique_UserAgents_parsed.xlsx).

Afterwards, some statistics are calculated to verify the shares in the data among the Operative Systems, browsers and device type used. The script then outputs three Excel tables, one for each share (OS, browser, device type) and plots the data graphically with pie charts.

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
