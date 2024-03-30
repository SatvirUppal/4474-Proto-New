# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 1080)
        MainWindow.setMinimumSize(QSize(607, 1080))
        MainWindow.setMaximumSize(QSize(607, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 570, 1818))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 1800))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 10, 431, 31))
        self.gridSearch = QGridLayout(self.gridLayoutWidget)
        self.gridSearch.setObjectName(u"gridSearch")
        self.gridSearch.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridSearch.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridSearch.addWidget(self.pushButton, 0, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 60, 602, 251))
        self.gridCurrent = QGridLayout(self.gridLayoutWidget_3)
        self.gridCurrent.setObjectName(u"gridCurrent")
        self.gridCurrent.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 2, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(7)
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 3, 2, 1)

        self.horizontalSpacer = QSpacerItem(200, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 2, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 4, 2, 1)

        self.gridLayout_2.setColumnStretch(4, 10)

        self.gridCurrent.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.frame)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 320, 551, 331))
        self.gridHourly = QGridLayout(self.gridLayoutWidget_4)
        self.gridHourly.setObjectName(u"gridHourly")
        self.gridHourly.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.gridLayoutWidget_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridHourly.addWidget(self.line_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridHourly.addWidget(self.label_6, 1, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridHourly.addWidget(self.line, 3, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.gridLayoutWidget_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1018, 270))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(1000, 250))
        self.frame_2.setMaximumSize(QSize(1000, 250))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_9.addWidget(self.label_20)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_9.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_9.addWidget(self.label_23)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_9.addWidget(self.label_25)


        self.gridLayout.addLayout(self.verticalLayout_9, 0, 2, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_12.addWidget(self.label_28)

        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_12.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_12.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_12.addWidget(self.label_33)


        self.gridLayout.addLayout(self.verticalLayout_12, 0, 4, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_11.addWidget(self.label_15)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_11.addWidget(self.label_18)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_11.addWidget(self.label_21)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_11.addWidget(self.label_24)


        self.gridLayout.addLayout(self.verticalLayout_11, 0, 3, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_10.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_10.addWidget(self.label_27)

        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_10.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_10.addWidget(self.label_30)


        self.gridLayout.addLayout(self.verticalLayout_10, 0, 6, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_8.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_8.addWidget(self.label_17)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_8.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_8, 0, 1, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_13.addWidget(self.label_34)

        self.label_75 = QLabel(self.frame_2)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout_13.addWidget(self.label_75)

        self.label_94 = QLabel(self.frame_2)
        self.label_94.setObjectName(u"label_94")

        self.verticalLayout_13.addWidget(self.label_94)

        self.label_95 = QLabel(self.frame_2)
        self.label_95.setObjectName(u"label_95")

        self.verticalLayout_13.addWidget(self.label_95)


        self.gridLayout.addLayout(self.verticalLayout_13, 0, 5, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridHourly.addWidget(self.scrollArea_2, 2, 0, 1, 1)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(0, 640, 551, 101))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_35.setFont(font2)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_6 = QWidget(self.frame)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 730, 551, 361))
        self.gridMultipleDay = QGridLayout(self.gridLayoutWidget_6)
        self.gridMultipleDay.setObjectName(u"gridMultipleDay")
        self.gridMultipleDay.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.gridLayoutWidget_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridMultipleDay.addWidget(self.line_3, 0, 0, 1, 1)

        self.scrollArea_3 = QScrollArea(self.gridLayoutWidget_6)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1018, 273))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(1000, 250))
        self.frame_3.setMaximumSize(QSize(1000, 250))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_61 = QLabel(self.frame_3)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_5.addWidget(self.label_61, 0, 1, 1, 1)

        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_5.addWidget(self.label_39, 0, 3, 1, 1)

        self.label_40 = QLabel(self.frame_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_5.addWidget(self.label_40, 0, 4, 1, 1)

        self.label_53 = QLabel(self.frame_3)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_5.addWidget(self.label_53, 0, 0, 1, 1)

        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_5.addWidget(self.label_45, 0, 6, 1, 1)

        self.label_60 = QLabel(self.frame_3)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_5.addWidget(self.label_60, 0, 5, 1, 1)

        self.label_46 = QLabel(self.frame_3)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_5.addWidget(self.label_46, 0, 2, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_38 = QLabel(self.frame_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 1, 1, 1, 1)

        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 1, 0, 1, 1)

        self.label_41 = QLabel(self.frame_3)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_42 = QLabel(self.frame_3)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_6.addWidget(self.label_42, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_43 = QLabel(self.frame_3)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_7.addWidget(self.label_43, 1, 1, 1, 1)

        self.label_44 = QLabel(self.frame_3)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_7.addWidget(self.label_44, 1, 0, 1, 1)

        self.label_47 = QLabel(self.frame_3)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_7.addWidget(self.label_47, 0, 0, 1, 1)

        self.label_48 = QLabel(self.frame_3)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_7.addWidget(self.label_48, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_7, 1, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_49 = QLabel(self.frame_3)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_8.addWidget(self.label_49, 1, 1, 1, 1)

        self.label_50 = QLabel(self.frame_3)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_8.addWidget(self.label_50, 1, 0, 1, 1)

        self.label_51 = QLabel(self.frame_3)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_8.addWidget(self.label_51, 0, 0, 1, 1)

        self.label_52 = QLabel(self.frame_3)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_8.addWidget(self.label_52, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_8, 1, 2, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_54 = QLabel(self.frame_3)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_9.addWidget(self.label_54, 1, 1, 1, 1)

        self.label_55 = QLabel(self.frame_3)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_9.addWidget(self.label_55, 1, 0, 1, 1)

        self.label_56 = QLabel(self.frame_3)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_9.addWidget(self.label_56, 0, 0, 1, 1)

        self.label_57 = QLabel(self.frame_3)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_9.addWidget(self.label_57, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_9, 1, 3, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_58 = QLabel(self.frame_3)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_10.addWidget(self.label_58, 1, 1, 1, 1)

        self.label_59 = QLabel(self.frame_3)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_10.addWidget(self.label_59, 1, 0, 1, 1)

        self.label_62 = QLabel(self.frame_3)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_10.addWidget(self.label_62, 0, 0, 1, 1)

        self.label_63 = QLabel(self.frame_3)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_10.addWidget(self.label_63, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_10, 1, 4, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_64 = QLabel(self.frame_3)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_11.addWidget(self.label_64, 1, 1, 1, 1)

        self.label_65 = QLabel(self.frame_3)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_11.addWidget(self.label_65, 1, 0, 1, 1)

        self.label_66 = QLabel(self.frame_3)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_11.addWidget(self.label_66, 0, 0, 1, 1)

        self.label_67 = QLabel(self.frame_3)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_11.addWidget(self.label_67, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_11, 1, 5, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_68 = QLabel(self.frame_3)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_12.addWidget(self.label_68, 1, 1, 1, 1)

        self.label_69 = QLabel(self.frame_3)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_12.addWidget(self.label_69, 1, 0, 1, 1)

        self.label_70 = QLabel(self.frame_3)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_12.addWidget(self.label_70, 0, 0, 1, 1)

        self.label_71 = QLabel(self.frame_3)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_12.addWidget(self.label_71, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_12, 1, 6, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_5)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.gridMultipleDay.addWidget(self.scrollArea_3, 3, 0, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridMultipleDay.addWidget(self.line_4, 4, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_6)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.gridMultipleDay.addWidget(self.comboBox, 2, 0, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridMultipleDay.addWidget(self.label_36, 1, 0, 1, 1)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(0, 1100, 551, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_14 = QWidget(self.frame)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(-1, 1119, 561, 431))
        self.gridMetrics = QGridLayout(self.gridLayoutWidget_14)
        self.gridMetrics.setObjectName(u"gridMetrics")
        self.gridMetrics.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_80 = QLabel(self.gridLayoutWidget_14)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_15.addWidget(self.label_80, 1, 0, 1, 1)

        self.label_81 = QLabel(self.gridLayoutWidget_14)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_15.addWidget(self.label_81, 1, 1, 1, 1)

        self.label_82 = QLabel(self.gridLayoutWidget_14)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_15.addWidget(self.label_82, 0, 0, 1, 2)


        self.gridMetrics.addLayout(self.gridLayout_15, 1, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_83 = QLabel(self.gridLayoutWidget_14)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_16.addWidget(self.label_83, 1, 0, 1, 1)

        self.label_84 = QLabel(self.gridLayoutWidget_14)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_16.addWidget(self.label_84, 1, 1, 1, 1)

        self.label_77 = QLabel(self.gridLayoutWidget_14)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_16.addWidget(self.label_77, 0, 0, 1, 2)


        self.gridMetrics.addLayout(self.gridLayout_16, 1, 2, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_85 = QLabel(self.gridLayoutWidget_14)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_17.addWidget(self.label_85, 1, 0, 1, 1)

        self.label_86 = QLabel(self.gridLayoutWidget_14)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_17.addWidget(self.label_86, 1, 1, 1, 1)

        self.label_87 = QLabel(self.gridLayoutWidget_14)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_17.addWidget(self.label_87, 0, 0, 1, 2)


        self.gridMetrics.addLayout(self.gridLayout_17, 0, 2, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_78 = QLabel(self.gridLayoutWidget_14)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_14.addWidget(self.label_78, 1, 0, 1, 1)

        self.label_79 = QLabel(self.gridLayoutWidget_14)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_14.addWidget(self.label_79, 1, 1, 1, 1)

        self.label_76 = QLabel(self.gridLayoutWidget_14)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_14.addWidget(self.label_76, 0, 0, 1, 2)


        self.gridMetrics.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_88 = QLabel(self.gridLayoutWidget_14)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_18.addWidget(self.label_88, 1, 0, 1, 1)

        self.label_89 = QLabel(self.gridLayoutWidget_14)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_18.addWidget(self.label_89, 1, 1, 1, 1)

        self.label_90 = QLabel(self.gridLayoutWidget_14)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_18.addWidget(self.label_90, 0, 0, 1, 2)


        self.gridMetrics.addLayout(self.gridLayout_18, 1, 1, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_91 = QLabel(self.gridLayoutWidget_14)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_19.addWidget(self.label_91, 1, 0, 1, 1)

        self.label_92 = QLabel(self.gridLayoutWidget_14)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_19.addWidget(self.label_92, 1, 1, 1, 1)

        self.label_93 = QLabel(self.gridLayoutWidget_14)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_19.addWidget(self.label_93, 0, 0, 1, 2)


        self.gridMetrics.addLayout(self.gridLayout_19, 0, 1, 1, 1)

        self.gridLayoutWidget_21 = QWidget(self.frame)
        self.gridLayoutWidget_21.setObjectName(u"gridLayoutWidget_21")
        self.gridLayoutWidget_21.setGeometry(QRect(0, 1580, 561, 211))
        self.gridSunriseSet = QGridLayout(self.gridLayoutWidget_21)
        self.gridSunriseSet.setObjectName(u"gridSunriseSet")
        self.gridSunriseSet.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.gridLayoutWidget_21)
        self.label_74.setObjectName(u"label_74")

        self.gridSunriseSet.addWidget(self.label_74, 0, 0, 1, 1)

        self.label_72 = QLabel(self.gridLayoutWidget_21)
        self.label_72.setObjectName(u"label_72")

        self.gridSunriseSet.addWidget(self.label_72, 1, 0, 1, 1)

        self.label_73 = QLabel(self.gridLayoutWidget_21)
        self.label_73.setObjectName(u"label_73")

        self.gridSunriseSet.addWidget(self.label_73, 0, 1, 2, 1)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 1550, 551, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 607, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRadar = QMenu(self.menubar)
        self.menuRadar.setObjectName(u"menuRadar")
        self.menuNews = QMenu(self.menubar)
        self.menuNews.setObjectName(u"menuNews")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRadar.menuAction())
        self.menubar.addAction(self.menuNews.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for a location...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Temperature", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TempLowDay", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TempHighDay", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wimage", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hourly Forecast", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"precipitationImage", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"precipitationImage", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"precipitationImage", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"precipitationImage", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"precipitationImage", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"precipitationImage", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"precipitationImage", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ad Container", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"WImage", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"WImage", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"WImage", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"WImage", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"WImage", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"WImage", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"WImage", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Days", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Weather Forecast", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Metric Name", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Metric Name", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Metric Name", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Metric Name", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Metric Name", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Metric Name", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Sunrise Time", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Sunset Time", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Sunrise/Sunset Icon", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Home", None))
        self.menuRadar.setTitle(QCoreApplication.translate("MainWindow", u"Radar", None))
        self.menuNews.setTitle(QCoreApplication.translate("MainWindow", u"News", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

