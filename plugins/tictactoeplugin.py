# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
#from __future__ import annotations

import os
plugins = os.environ['PYSIDE_DESIGNER_PLUGINS']

from tictactoe import TicTacToe

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtDesigner import QDesignerCustomWidgetInterface


DOM_XML = """
<ui language='c++'>
    <widget class='TicTacToe' name='ticTacToe'>
        <property name='geometry'>
            <rect>
                <x>0</x>
                <y>0</y>
                <width>200</width>
                <height>200</height>
            </rect>
        </property>
        <property name='state'>
            <string>-X-XO----</string>
        </property>
    </widget>
</ui>
"""

class TicTacToePlugin(QDesignerCustomWidgetInterface):
    def __init__(self):
        super().__init__()

        self.initialized = False

    def createWidget(self, parent):
        t = TicTacToe(parent)
        return t

    def domXml(self):
        return DOM_XML

    def group(self):
        return ''

    def icon(self):
        return QPixmap(plugins+'/images/tic-tac-toe.png')

    def includeFile(self):
        return 'tictactoe'

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isContainer(self):
        return False

    def isInitialized(self):
        return self.initialized

    def name(self):
        return 'TicTacToe'

    def toolTip(self):
        return 'Tic Tac Toe Example, demonstrating class QDesignerTaskMenuExtension (Python)'

    def whatsThis(self):
        return self.toolTip()
