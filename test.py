# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerJgkgGt.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QDoubleValidator, QKeyEvent)

from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QTimeEdit,
    QSizePolicy, QStatusBar, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem, QCheckBox)

#import sys
#sys.path.insert(0, "/home/brad/git/Qt-plugin/plugins")

from plugins.analogclock import PyAnalogClock

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 301)
        #MainWindow.setWindowTitle('Analog Clock')
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.analogClock = PyAnalogClock(parent=self.centralwidget)
        self.analogClock.setMinimumSize(QSize(250, 250))
        self.analogClock.setObjectName("analogClock")
        self.verticalLayout.addWidget(self.analogClock)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QSize(70, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.timeEdit = QTimeEdit(parent=self.centralwidget)
        self.timeEdit.setMaximumSize(QSize(55, 20))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout.addWidget(self.timeEdit)
        self.checkBox = QCheckBox(parent=self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.timeEdit.userTimeChanged.connect(self.setOffset)
        self.checkBox.checkStateChanged.connect(self.checkStateChanged)
        QMetaObject.connectSlotsByName(MainWindow)


    def keyPressEvent(self, event):
        print('keyPress')
        if isinstance(event, QKeyEvent):
            key_text = event.text()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Clock Test"))
#if QT_CONFIG(tooltip)
        #self.PyanalogClock.setToolTip(QCoreApplication.translate("MainWindow", u"The current time", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        #self.PyanalogClock.setWhatsThis(QCoreApplication.translate("MainWindow", u"The analog clock widget displays the current time.", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zone offset:", None))
        #self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        pass
    # retranslateUi

    def setOffset(self, time=None):
        #print('set zone')
        offset = time.hour()*60+time.minute()
        self.analogClock.timeZoneOffset = offset
        self.analogClock.update()

    def checkStateChanged(self, state=None):
        self.analogClock.drawHand = self.checkBox.isChecked()
        self.analogClock.update()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        #print('keyPress')
        if isinstance(event, QKeyEvent):
            #key = event.key()
            mod = event.nativeModifiers()
            #scan = event.nativeScanCode()
            vert = event.nativeVirtualKey()
            asc = vert & 0xff
            #print('key', hex(key), mod, scan, vert, asc)
            if asc == 27 and mod ==4:
               QApplication.quit()

if __name__ == "__main__":
    import sys

    app =  QApplication(sys.argv)
    main = Main()

    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()

    sys.exit(app.exec())

