# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations

from analogclock import PyAnalogClock  # noqa: F401
from analogclockplugin import AnalogClockPlugin

from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection

# Set PYSIDE_DESIGNER_PLUGINS to point to this directory and load the plugin


if __name__ == '__main__':
    QPyDesignerCustomWidgetCollection.addCustomWidget(AnalogClockPlugin())
