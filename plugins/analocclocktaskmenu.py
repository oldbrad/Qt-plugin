# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations

from analogclock import AnalogClock

from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout
from PySide6.QtDesigner import (QExtensionFactory, QPyDesignerTaskMenuExtension)


class AnalogClockDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self._analClock = TicTacToe(self)
        layout.addWidget(self._analClock)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                                      | QDialogButtonBox.StandardButton.Cancel
                                      | QDialogButtonBox.StandardButton.Reset)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        reset_button = button_box.button(QDialogButtonBox.StandardButton.Reset)
        reset_button.clicked.connect(self._analClock.clear_board)
        layout.addWidget(button_box)

    def set_state(self, new_state):
        self._analClock.setState(new_state)

    def state(self):
        return self._analClock.state


class AnalogClockMenu(QPyDesignerTaskMenuExtension):
    def __init__(self, analogClock, parent):
        super().__init__(parent)
        self._analClock = analogClock
        self._edit_state_action = QAction('Edit State...', None)
        self._edit_state_action.triggered.connect(self._edit_state)

    def taskActions(self):
        return [self._edit_state_action]

    def preferredEditAction(self):
        return self._edit_state_action

    @Slot()
    def _edit_state(self):
        dialog = AnalogClockDialog(self._analClock)
        dialog.set_state(self._analClock.state)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self._analClock.state = dialog.state()


class AnalogClockkMenuFactory(QExtensionFactory):
    def __init__(self, extension_manager):
        super().__init__(extension_manager)

    @staticmethod
    def task_menu_iid():
        return 'org.qt-project.Qt.Designer.TaskMenu'

    def createExtension(self, object, iid, parent):
        if iid != AnalogClockkMenuFactory.task_menu_iid():
            return None
        if object.__class__.__name__ != 'TicTacToe':
            return None
        return AnalogClockMenu(object, parent)
