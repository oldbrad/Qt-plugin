# Qt-plugins

 This archive provides examples of a python 'plugins' for Qt designer. The provided examples are a modified version of the original PyAnalogClock.py example distributed with PyQt5 and unmodified tic-tac-toe.py

 Inspired by MadQt MadQtPluginCreator, which does not work under Linux. Creating plugins is completely obscure, but relativly simple once seen.
 
## Note

 A plugin consists of three pieces: two python scripts and an entry in register.py
 
 For example, analogclock.py, analogclockplugin.py and lines 6 and 7 in register.py
 
## Prerequisites

 Python 3.12 and pip or uv
  
 You must set the environment variable PYSIDE_DESIGNER_PLUGINS to point to the downloaded plugins directory.
 
 ## Inatall PySide6 and pyside6-designer
 
 The installation should be done from pypi.org into a python virtual environment using your prefered method. I use pip because thats what I learned first.
 
  brad@dell:~ $  mkdir test  
  brad@dell:~ $ python3 -m venv test  
  brad@dell:~ $ source test/bin/activate  
  (test)brad@dell:~ $ pip install PySide6  
  (test)brad@dell:~ $ which pyside6-designer  
  /home/brad/test/bin/pyside6-designer
  
## Configure and Run Designer

 Configure the environment variable.  
 (test)brad@dell:~ $ export PYSIDE_DESIGNER_PLUGINS=Qt-plugin/plugins

 Now run Qt Designer using pyside6-designer, not your package manager version.  
 (test)brad@dell:~ $ pyside6-designer

You should then see Custom Widgets with the PyAnalogClock and tic-tac-tow  items in designers left side Widget Box

Also Help > About Plugins should also display the plugins.
 
