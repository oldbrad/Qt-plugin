# Qt-plugins
An  example of  PySide6 plugin for Qt dsigner.
The necessary source files are in the plugins directory.

Required PySide6 and designer version 6.11 This will not work with PyQt6 or designer v5.
 
## Add plugins to designer

It is convenient to create a ptyhon vertual environment and if necessary pip install Pyside6
 
 Execute the next in a bash shell

   $ $ python3 -m venv env
   $ source env/bin/activate
   (env)$ export PYSIDE_DESIGNER_PLUGINS=/home/brad/work/qt/plugins
   (env)$ pyside6-designer
 
 Setting the environment variable PYSIDE_DESIGNER_PLUGINS correctly is crucal.

 You should no see Custom widgets with the PyAnalogClock item. 
 
