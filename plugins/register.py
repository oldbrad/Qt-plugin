# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection

from analogclockplugin import AnalogClockPlugin
QPyDesignerCustomWidgetCollection.addCustomWidget(AnalogClockPlugin())

from tictactoeplugin import TicTacToePlugin
QPyDesignerCustomWidgetCollection.addCustomWidget(TicTacToePlugin())
