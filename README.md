# Qt-plugins

 This archive provides examples of a python 'plugins' for Qt designer. The provided examples are a modified version of the original PyAnalogClock.py example distributed with PyQt5 and unmodified tic-tac-toe.py

 Inspired by MadQt MadQtPluginCreator, which does not work under Linux. Creating plugins is completely obscure, but relativly simple once seen.
 
## Note

 A plugin consists of three pieces: two python scripts and an entry in register.py
 
 For example, analogclock.py, analogclockplugin.py and lines 6 and 7 in register.py
 
## Prerequisites

 PySide6
 Qt Designer version 6.11
 
 You must set the environment variable PYSIDE_DESIGNER_PLUGINS to point to the downloaded plugins directory.
 
## Configure and Run Designer

Configure the environment variable.
 $ export PYSIDE_DESIGNER_PLUGINS=Qt-plugin/plugins

Now run Qt Designer using pyside6-designer, not your package manager version.

In my case Designer is in the vertual environment in which I installed PySidey6
(env):~$ /home/brad/env/bin/pyside6-designer

You should then see Custom widgets with the PyAnalogClock and tic-tac-tow  items in designers left Widget Box

Also Help > About Plugins should also display the plugins.
 
