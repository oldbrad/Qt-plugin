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
    QSizePolicy, QStatusBar, QWidget, QFrame, QHBoxLayout, QSpacerItem)

from analogclock import PyAnalogClock

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #if not MainWindow.objectName():
        #    MainWindow.setObjectName(u"MainWindow")
        #MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        #MainWindow.resize(400, 400)
        MainWindow.setFixedSize(264, 285)
        #MainWindow.setMaximumSize(QSize(400, 16777215))
        MainWindow.setWindowTitle(u"Qt Clock")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(2, 2, 260, 270))
        self.frame.setStyleSheet(u"QFrame, QLabel, QToolTip {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.PyanalogClock = PyAnalogClock(self.frame)
        self.PyanalogClock.setObjectName(u"PyanalogClock")
        self.PyanalogClock.setGeometry(QRect(5, 5, 250, 250))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PyanalogClock.sizePolicy().hasHeightForWidth())
        self.PyanalogClock.setSizePolicy(sizePolicy)
        self.PyanalogClock.setMinimumSize(QSize(0, 0))
        self.PyanalogClock.setMaximumSize(QSize(250, 250))
        self.PyanalogClock.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 254, 235, 24))

        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 30, 0)
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label.setIndent(-3)

        self.horizontalLayout.addWidget(self.label)


        self.timeEdit = QTimeEdit(self.widget)
        self.timeEdit.setFixedWidth(60)

        self.horizontalLayout.addWidget(self.timeEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        #self.statusbar = QStatusBar(MainWindow)
        #self.statusbar.setObjectName(u"statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.timeEdit.userTimeChanged.connect(self.setOffset)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def keyPressEvent(self, event):
        print('keyPress')
        if isinstance(event, QKeyEvent):
            key_text = event.text()

    def retranslateUi(self, MainWindow):
#if QT_CONFIG(tooltip)
        #self.PyanalogClock.setToolTip(QCoreApplication.translate("MainWindow", u"The current time", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        #self.PyanalogClock.setWhatsThis(QCoreApplication.translate("MainWindow", u"The analog clock widget displays the current time.", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zone offset:", None))
        #self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        pass
    # retranslateUi

    def setOffset(self, time=None):
        offset = time.hour()+time.minute()/60.0
        self.PyanalogClock.timeZoneOffset = offset
        self.PyanalogClock.update()

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
    #main = QMainWindow()
    main = Main()

    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()

    sys.exit(app.exec())

