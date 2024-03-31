# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'news.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_NewsWindow(object):
    def setupUi(self, NewsWindow):
        if not NewsWindow.objectName():
            NewsWindow.setObjectName(u"NewsWindow")
        NewsWindow.resize(607, 1080)
        NewsWindow.setMinimumSize(QSize(607, 1080))
        NewsWindow.setMaximumSize(QSize(607, 1080))
        self.centralwidget = QWidget(NewsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 10, 231, 91))
        NewsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NewsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 607, 43))
        NewsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NewsWindow)
        self.statusbar.setObjectName(u"statusbar")
        NewsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewsWindow)

        QMetaObject.connectSlotsByName(NewsWindow)
    # setupUi

    def retranslateUi(self, NewsWindow):
        NewsWindow.setWindowTitle(QCoreApplication.translate("NewsWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("NewsWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700;\">News: <br />Weather Inc.</span></p></body></html>", None))
    # retranslateUi

