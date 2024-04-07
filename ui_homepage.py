# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepage.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 950)
        MainWindow.setMinimumSize(QSize(607, 950))
        MainWindow.setMaximumSize(QSize(607, 950))
        font = QFont()
        font.setFamilies([u"Geneva"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 591, 911))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.verticalLayoutWidget = QWidget(self.Page1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 19, 591, 831))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, -291, 572, 1873))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.searchGrid = QGridLayout()
        self.searchGrid.setObjectName(u"searchGrid")
        self.search_btn = QPushButton(self.scrollAreaWidgetContents_8)
        self.search_btn.setObjectName(u"search_btn")

        self.searchGrid.addWidget(self.search_btn, 0, 1, 1, 1)

        self.search_entry = QLineEdit(self.scrollAreaWidgetContents_8)
        self.search_entry.setObjectName(u"search_entry")
        self.search_entry.setMaxLength(100)
        self.search_entry.setFrame(False)

        self.searchGrid.addWidget(self.search_entry, 0, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.searchGrid)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setMinimumSize(QSize(0, 1800))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_11 = QWidget(self.frame_7)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(0, 320, 551, 341))
        self.gridHourly_3 = QGridLayout(self.gridLayoutWidget_11)
        self.gridHourly_3.setObjectName(u"gridHourly_3")
        self.gridHourly_3.setContentsMargins(0, 0, 0, 0)
        self.hourlyTimeLine = QScrollArea(self.gridLayoutWidget_11)
        self.hourlyTimeLine.setObjectName(u"hourlyTimeLine")
        self.hourlyTimeLine.setEnabled(True)
        self.hourlyTimeLine.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hourlyTimeLine.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.hourlyTimeLine.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setEnabled(True)
        self.scrollAreaWidgetContents_9.setGeometry(QRect(-35, 0, 1010, 271))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(1000, 250))
        self.frame_8.setMaximumSize(QSize(1000, 250))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.line_19 = QFrame(self.frame_8)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.gridLayout_36.addWidget(self.line_19, 0, 7, 1, 1)

        self.hour3 = QVBoxLayout()
        self.hour3.setObjectName(u"hour3")
        self.time_3 = QLabel(self.frame_8)
        self.time_3.setObjectName(u"time_3")
        font1 = QFont()
        font1.setFamilies([u"Geneva"])
        font1.setPointSize(14)
        self.time_3.setFont(font1)
        self.time_3.setAlignment(Qt.AlignCenter)

        self.hour3.addWidget(self.time_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temp_3 = QLabel(self.frame_8)
        self.temp_3.setObjectName(u"temp_3")
        self.temp_3.setAlignment(Qt.AlignCenter)

        self.hour3.addWidget(self.temp_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.image_3 = QLabel(self.frame_8)
        self.image_3.setObjectName(u"image_3")
        self.image_3.setMaximumSize(QSize(75, 67))
        self.image_3.setScaledContents(True)
        self.image_3.setAlignment(Qt.AlignCenter)

        self.hour3.addWidget(self.image_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipImage_8 = QLabel(self.frame_8)
        self.percipImage_8.setObjectName(u"percipImage_8")
        self.percipImage_8.setMinimumSize(QSize(30, 30))
        self.percipImage_8.setMaximumSize(QSize(30, 30))
        self.percipImage_8.setTextFormat(Qt.AutoText)
        self.percipImage_8.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_8.setScaledContents(True)
        self.percipImage_8.setAlignment(Qt.AlignCenter)
        self.percipImage_8.setIndent(0)

        self.hour3.addWidget(self.percipImage_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipPer_3 = QLabel(self.frame_8)
        self.percipPer_3.setObjectName(u"percipPer_3")
        self.percipPer_3.setAlignment(Qt.AlignCenter)

        self.hour3.addWidget(self.percipPer_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_36.addLayout(self.hour3, 0, 4, 1, 1)

        self.hour6 = QVBoxLayout()
        self.hour6.setObjectName(u"hour6")
        self.time_6 = QLabel(self.frame_8)
        self.time_6.setObjectName(u"time_6")
        self.time_6.setFont(font1)
        self.time_6.setAlignment(Qt.AlignCenter)

        self.hour6.addWidget(self.time_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temp_6 = QLabel(self.frame_8)
        self.temp_6.setObjectName(u"temp_6")
        self.temp_6.setAlignment(Qt.AlignCenter)

        self.hour6.addWidget(self.temp_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.image_6 = QLabel(self.frame_8)
        self.image_6.setObjectName(u"image_6")
        self.image_6.setMaximumSize(QSize(75, 75))
        self.image_6.setScaledContents(True)
        self.image_6.setAlignment(Qt.AlignCenter)

        self.hour6.addWidget(self.image_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipImage_11 = QLabel(self.frame_8)
        self.percipImage_11.setObjectName(u"percipImage_11")
        self.percipImage_11.setMinimumSize(QSize(30, 30))
        self.percipImage_11.setMaximumSize(QSize(30, 30))
        self.percipImage_11.setTextFormat(Qt.AutoText)
        self.percipImage_11.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_11.setScaledContents(True)
        self.percipImage_11.setAlignment(Qt.AlignCenter)
        self.percipImage_11.setIndent(0)

        self.hour6.addWidget(self.percipImage_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipPer_6 = QLabel(self.frame_8)
        self.percipPer_6.setObjectName(u"percipPer_6")
        self.percipPer_6.setAlignment(Qt.AlignCenter)

        self.hour6.addWidget(self.percipPer_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_36.addLayout(self.hour6, 0, 10, 1, 1)

        self.line_20 = QFrame(self.frame_8)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.gridLayout_36.addWidget(self.line_20, 0, 9, 1, 1)

        self.hour5 = QVBoxLayout()
        self.hour5.setObjectName(u"hour5")
        self.time_5 = QLabel(self.frame_8)
        self.time_5.setObjectName(u"time_5")
        self.time_5.setFont(font1)
        self.time_5.setAlignment(Qt.AlignCenter)

        self.hour5.addWidget(self.time_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temp_5 = QLabel(self.frame_8)
        self.temp_5.setObjectName(u"temp_5")
        self.temp_5.setAlignment(Qt.AlignCenter)

        self.hour5.addWidget(self.temp_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.image_5 = QLabel(self.frame_8)
        self.image_5.setObjectName(u"image_5")
        self.image_5.setMaximumSize(QSize(75, 75))
        self.image_5.setScaledContents(True)
        self.image_5.setAlignment(Qt.AlignCenter)

        self.hour5.addWidget(self.image_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipImage_10 = QLabel(self.frame_8)
        self.percipImage_10.setObjectName(u"percipImage_10")
        self.percipImage_10.setMinimumSize(QSize(30, 30))
        self.percipImage_10.setMaximumSize(QSize(30, 30))
        self.percipImage_10.setTextFormat(Qt.AutoText)
        self.percipImage_10.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_10.setScaledContents(True)
        self.percipImage_10.setAlignment(Qt.AlignCenter)
        self.percipImage_10.setIndent(0)

        self.hour5.addWidget(self.percipImage_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipPer_5 = QLabel(self.frame_8)
        self.percipPer_5.setObjectName(u"percipPer_5")
        self.percipPer_5.setAlignment(Qt.AlignCenter)

        self.hour5.addWidget(self.percipPer_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_36.addLayout(self.hour5, 0, 8, 1, 1)

        self.line_11 = QFrame(self.frame_8)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_36.addWidget(self.line_11, 0, 3, 1, 1)

        self.hour7 = QVBoxLayout()
        self.hour7.setObjectName(u"hour7")
        self.time_7 = QLabel(self.frame_8)
        self.time_7.setObjectName(u"time_7")
        self.time_7.setFont(font1)
        self.time_7.setAlignment(Qt.AlignCenter)

        self.hour7.addWidget(self.time_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temp_7 = QLabel(self.frame_8)
        self.temp_7.setObjectName(u"temp_7")
        self.temp_7.setAlignment(Qt.AlignCenter)

        self.hour7.addWidget(self.temp_7, 0, Qt.AlignVCenter)

        self.image_7 = QLabel(self.frame_8)
        self.image_7.setObjectName(u"image_7")
        self.image_7.setMaximumSize(QSize(75, 75))
        self.image_7.setScaledContents(True)
        self.image_7.setAlignment(Qt.AlignCenter)

        self.hour7.addWidget(self.image_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipImage_12 = QLabel(self.frame_8)
        self.percipImage_12.setObjectName(u"percipImage_12")
        self.percipImage_12.setMinimumSize(QSize(30, 30))
        self.percipImage_12.setMaximumSize(QSize(30, 30))
        self.percipImage_12.setTextFormat(Qt.AutoText)
        self.percipImage_12.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_12.setScaledContents(True)
        self.percipImage_12.setAlignment(Qt.AlignCenter)
        self.percipImage_12.setIndent(0)

        self.hour7.addWidget(self.percipImage_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipPer_7 = QLabel(self.frame_8)
        self.percipPer_7.setObjectName(u"percipPer_7")
        self.percipPer_7.setAlignment(Qt.AlignCenter)

        self.hour7.addWidget(self.percipPer_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_36.addLayout(self.hour7, 0, 12, 1, 1)

        self.hour2 = QVBoxLayout()
        self.hour2.setObjectName(u"hour2")
        self.time_2 = QLabel(self.frame_8)
        self.time_2.setObjectName(u"time_2")
        self.time_2.setFont(font1)
        self.time_2.setAlignment(Qt.AlignCenter)

        self.hour2.addWidget(self.time_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temp_2 = QLabel(self.frame_8)
        self.temp_2.setObjectName(u"temp_2")
        self.temp_2.setAlignment(Qt.AlignCenter)

        self.hour2.addWidget(self.temp_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.image_2 = QLabel(self.frame_8)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setMaximumSize(QSize(75, 75))
        self.image_2.setScaledContents(True)
        self.image_2.setAlignment(Qt.AlignCenter)

        self.hour2.addWidget(self.image_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipImage_2 = QLabel(self.frame_8)
        self.percipImage_2.setObjectName(u"percipImage_2")
        self.percipImage_2.setMinimumSize(QSize(30, 30))
        self.percipImage_2.setMaximumSize(QSize(30, 30))
        self.percipImage_2.setTextFormat(Qt.AutoText)
        self.percipImage_2.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_2.setScaledContents(True)
        self.percipImage_2.setAlignment(Qt.AlignCenter)
        self.percipImage_2.setIndent(0)

        self.hour2.addWidget(self.percipImage_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipPer_2 = QLabel(self.frame_8)
        self.percipPer_2.setObjectName(u"percipPer_2")
        self.percipPer_2.setAlignment(Qt.AlignCenter)

        self.hour2.addWidget(self.percipPer_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_36.addLayout(self.hour2, 0, 2, 1, 1)

        self.line_21 = QFrame(self.frame_8)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.gridLayout_36.addWidget(self.line_21, 0, 11, 1, 1)

        self.hour4 = QVBoxLayout()
        self.hour4.setObjectName(u"hour4")
        self.time_4 = QLabel(self.frame_8)
        self.time_4.setObjectName(u"time_4")
        self.time_4.setFont(font1)
        self.time_4.setAlignment(Qt.AlignCenter)

        self.hour4.addWidget(self.time_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temp_4 = QLabel(self.frame_8)
        self.temp_4.setObjectName(u"temp_4")
        self.temp_4.setAlignment(Qt.AlignCenter)

        self.hour4.addWidget(self.temp_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.image_4 = QLabel(self.frame_8)
        self.image_4.setObjectName(u"image_4")
        self.image_4.setMaximumSize(QSize(75, 75))
        self.image_4.setScaledContents(True)
        self.image_4.setAlignment(Qt.AlignCenter)

        self.hour4.addWidget(self.image_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipImage_9 = QLabel(self.frame_8)
        self.percipImage_9.setObjectName(u"percipImage_9")
        self.percipImage_9.setMinimumSize(QSize(30, 30))
        self.percipImage_9.setMaximumSize(QSize(30, 30))
        self.percipImage_9.setTextFormat(Qt.AutoText)
        self.percipImage_9.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_9.setScaledContents(True)
        self.percipImage_9.setAlignment(Qt.AlignCenter)
        self.percipImage_9.setIndent(0)

        self.hour4.addWidget(self.percipImage_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipPer_4 = QLabel(self.frame_8)
        self.percipPer_4.setObjectName(u"percipPer_4")
        self.percipPer_4.setAlignment(Qt.AlignCenter)

        self.hour4.addWidget(self.percipPer_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_36.addLayout(self.hour4, 0, 6, 1, 1)

        self.hour1 = QVBoxLayout()
        self.hour1.setObjectName(u"hour1")
        self.time_1 = QLabel(self.frame_8)
        self.time_1.setObjectName(u"time_1")
        self.time_1.setFont(font1)
        self.time_1.setAlignment(Qt.AlignCenter)

        self.hour1.addWidget(self.time_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.temp_1 = QLabel(self.frame_8)
        self.temp_1.setObjectName(u"temp_1")
        self.temp_1.setAlignment(Qt.AlignCenter)

        self.hour1.addWidget(self.temp_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.image_1 = QLabel(self.frame_8)
        self.image_1.setObjectName(u"image_1")
        self.image_1.setMaximumSize(QSize(75, 75))
        self.image_1.setScaledContents(True)
        self.image_1.setAlignment(Qt.AlignCenter)

        self.hour1.addWidget(self.image_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipImage_1 = QLabel(self.frame_8)
        self.percipImage_1.setObjectName(u"percipImage_1")
        self.percipImage_1.setMinimumSize(QSize(30, 30))
        self.percipImage_1.setMaximumSize(QSize(30, 30))
        self.percipImage_1.setTextFormat(Qt.AutoText)
        self.percipImage_1.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_1.setScaledContents(True)
        self.percipImage_1.setAlignment(Qt.AlignCenter)
        self.percipImage_1.setIndent(0)

        self.hour1.addWidget(self.percipImage_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.percipPer_1 = QLabel(self.frame_8)
        self.percipPer_1.setObjectName(u"percipPer_1")
        self.percipPer_1.setAlignment(Qt.AlignCenter)

        self.hour1.addWidget(self.percipPer_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_36.addLayout(self.hour1, 0, 0, 1, 1)

        self.line_12 = QFrame(self.frame_8)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_36.addWidget(self.line_12, 0, 5, 1, 1)

        self.line_10 = QFrame(self.frame_8)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_36.addWidget(self.line_10, 0, 1, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_36)


        self.verticalLayout_23.addWidget(self.frame_8)

        self.hourlyTimeLine.setWidget(self.scrollAreaWidgetContents_9)

        self.gridHourly_3.addWidget(self.hourlyTimeLine, 2, 0, 1, 1)

        self.hourlyLabel = QLabel(self.gridLayoutWidget_11)
        self.hourlyLabel.setObjectName(u"hourlyLabel")
        self.hourlyLabel.setAlignment(Qt.AlignCenter)

        self.gridHourly_3.addWidget(self.hourlyLabel, 1, 0, 1, 1)

        self.line_14 = QFrame(self.gridLayoutWidget_11)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridHourly_3.addWidget(self.line_14, 3, 0, 1, 1)

        self.line_13 = QFrame(self.gridLayoutWidget_11)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridHourly_3.addWidget(self.line_13, 0, 0, 1, 1)

        self.label_214 = QLabel(self.frame_7)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(0, 640, 551, 101))
        self.label_214.setMaximumSize(QSize(551, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Geneva"])
        font2.setPointSize(20)
        self.label_214.setFont(font2)
        self.label_214.setScaledContents(True)
        self.label_214.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_12 = QWidget(self.frame_7)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(0, 730, 551, 381))
        self.gridMultipleDay_3 = QGridLayout(self.gridLayoutWidget_12)
        self.gridMultipleDay_3.setObjectName(u"gridMultipleDay_3")
        self.gridMultipleDay_3.setContentsMargins(0, 0, 0, 0)
        self.line_15 = QFrame(self.gridLayoutWidget_12)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.gridMultipleDay_3.addWidget(self.line_15, 0, 0, 1, 1)

        self.chooseDay = QComboBox(self.gridLayoutWidget_12)
        self.chooseDay.addItem("")
        self.chooseDay.addItem("")
        self.chooseDay.addItem("")
        self.chooseDay.setObjectName(u"chooseDay")
        self.chooseDay.setEditable(False)
        self.chooseDay.setMaxVisibleItems(3)
        self.chooseDay.setMaxCount(3)

        self.gridMultipleDay_3.addWidget(self.chooseDay, 2, 0, 1, 1)

        self.line_16 = QFrame(self.gridLayoutWidget_12)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.gridMultipleDay_3.addWidget(self.line_16, 4, 0, 1, 1)

        self.label_250 = QLabel(self.gridLayoutWidget_12)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setAlignment(Qt.AlignCenter)

        self.gridMultipleDay_3.addWidget(self.label_250, 1, 0, 1, 1)

        self.muliDayScroll = QScrollArea(self.gridLayoutWidget_12)
        self.muliDayScroll.setObjectName(u"muliDayScroll")
        self.muliDayScroll.setEnabled(True)
        self.muliDayScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.muliDayScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.muliDayScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setEnabled(True)
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 1024, 275))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.multiDay = QFrame(self.scrollAreaWidgetContents_10)
        self.multiDay.setObjectName(u"multiDay")
        self.multiDay.setEnabled(True)
        sizePolicy.setHeightForWidth(self.multiDay.sizePolicy().hasHeightForWidth())
        self.multiDay.setSizePolicy(sizePolicy)
        self.multiDay.setMinimumSize(QSize(1000, 250))
        self.multiDay.setMaximumSize(QSize(1000, 250))
        self.multiDay.setStyleSheet(u"")
        self.multiDay.setFrameShape(QFrame.StyledPanel)
        self.multiDay.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.multiDay)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.day2Date = QLabel(self.multiDay)
        self.day2Date.setObjectName(u"day2Date")
        self.day2Date.setMinimumSize(QSize(100, 15))
        self.day2Date.setMaximumSize(QSize(100, 15))
        font3 = QFont()
        font3.setFamilies([u"Geneva"])
        font3.setPointSize(18)
        self.day2Date.setFont(font3)
        self.day2Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day2Date, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.day2Info = QGridLayout()
        self.day2Info.setObjectName(u"day2Info")
        self.day2TempLow = QLabel(self.multiDay)
        self.day2TempLow.setObjectName(u"day2TempLow")

        self.day2Info.addWidget(self.day2TempLow, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.day2Desc = QLabel(self.multiDay)
        self.day2Desc.setObjectName(u"day2Desc")
        self.day2Desc.setAlignment(Qt.AlignCenter)

        self.day2Info.addWidget(self.day2Desc, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.day2TempHi = QLabel(self.multiDay)
        self.day2TempHi.setObjectName(u"day2TempHi")

        self.day2Info.addWidget(self.day2TempHi, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.percipImage_5 = QLabel(self.multiDay)
        self.percipImage_5.setObjectName(u"percipImage_5")
        self.percipImage_5.setMinimumSize(QSize(30, 30))
        self.percipImage_5.setMaximumSize(QSize(30, 30))
        self.percipImage_5.setTextFormat(Qt.AutoText)
        self.percipImage_5.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_5.setScaledContents(True)
        self.percipImage_5.setAlignment(Qt.AlignCenter)
        self.percipImage_5.setIndent(0)

        self.day2Info.addWidget(self.percipImage_5, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_37.addLayout(self.day2Info, 2, 2, 1, 1)

        self.day4Info = QGridLayout()
        self.day4Info.setObjectName(u"day4Info")
        self.day4TempLow = QLabel(self.multiDay)
        self.day4TempLow.setObjectName(u"day4TempLow")

        self.day4Info.addWidget(self.day4TempLow, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.day4Desc = QLabel(self.multiDay)
        self.day4Desc.setObjectName(u"day4Desc")

        self.day4Info.addWidget(self.day4Desc, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.day4TempHi = QLabel(self.multiDay)
        self.day4TempHi.setObjectName(u"day4TempHi")

        self.day4Info.addWidget(self.day4TempHi, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.percipImage_7 = QLabel(self.multiDay)
        self.percipImage_7.setObjectName(u"percipImage_7")
        self.percipImage_7.setMinimumSize(QSize(30, 30))
        self.percipImage_7.setMaximumSize(QSize(30, 30))
        self.percipImage_7.setTextFormat(Qt.AutoText)
        self.percipImage_7.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_7.setScaledContents(True)
        self.percipImage_7.setAlignment(Qt.AlignCenter)
        self.percipImage_7.setIndent(0)

        self.day4Info.addWidget(self.percipImage_7, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_37.addLayout(self.day4Info, 2, 6, 1, 1)

        self.day6Info = QGridLayout()
        self.day6Info.setObjectName(u"day6Info")
        self.day6TempLow = QLabel(self.multiDay)
        self.day6TempLow.setObjectName(u"day6TempLow")

        self.day6Info.addWidget(self.day6TempLow, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.day6Desc = QLabel(self.multiDay)
        self.day6Desc.setObjectName(u"day6Desc")

        self.day6Info.addWidget(self.day6Desc, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.day6TempHi = QLabel(self.multiDay)
        self.day6TempHi.setObjectName(u"day6TempHi")

        self.day6Info.addWidget(self.day6TempHi, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.percipImage_14 = QLabel(self.multiDay)
        self.percipImage_14.setObjectName(u"percipImage_14")
        self.percipImage_14.setMinimumSize(QSize(30, 30))
        self.percipImage_14.setMaximumSize(QSize(30, 30))
        self.percipImage_14.setTextFormat(Qt.AutoText)
        self.percipImage_14.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_14.setScaledContents(True)
        self.percipImage_14.setAlignment(Qt.AlignCenter)
        self.percipImage_14.setIndent(0)

        self.day6Info.addWidget(self.percipImage_14, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_37.addLayout(self.day6Info, 2, 10, 1, 1)

        self.day1Date = QLabel(self.multiDay)
        self.day1Date.setObjectName(u"day1Date")
        self.day1Date.setMinimumSize(QSize(100, 15))
        self.day1Date.setMaximumSize(QSize(100, 15))
        self.day1Date.setFont(font3)
        self.day1Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day1Date, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.day3Date = QLabel(self.multiDay)
        self.day3Date.setObjectName(u"day3Date")
        self.day3Date.setMinimumSize(QSize(100, 15))
        self.day3Date.setMaximumSize(QSize(100, 15))
        self.day3Date.setFont(font3)
        self.day3Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day3Date, 0, 4, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.day1Info = QGridLayout()
        self.day1Info.setObjectName(u"day1Info")
        self.day1TempLow = QLabel(self.multiDay)
        self.day1TempLow.setObjectName(u"day1TempLow")

        self.day1Info.addWidget(self.day1TempLow, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.day1Desc = QLabel(self.multiDay)
        self.day1Desc.setObjectName(u"day1Desc")

        self.day1Info.addWidget(self.day1Desc, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.day1TempHi = QLabel(self.multiDay)
        self.day1TempHi.setObjectName(u"day1TempHi")

        self.day1Info.addWidget(self.day1TempHi, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.percipImage_3 = QLabel(self.multiDay)
        self.percipImage_3.setObjectName(u"percipImage_3")
        self.percipImage_3.setMinimumSize(QSize(30, 30))
        self.percipImage_3.setMaximumSize(QSize(30, 30))
        self.percipImage_3.setTextFormat(Qt.AutoText)
        self.percipImage_3.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_3.setScaledContents(True)
        self.percipImage_3.setAlignment(Qt.AlignCenter)
        self.percipImage_3.setIndent(0)

        self.day1Info.addWidget(self.percipImage_3, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_37.addLayout(self.day1Info, 2, 0, 1, 1)

        self.day4Image = QLabel(self.multiDay)
        self.day4Image.setObjectName(u"day4Image")
        self.day4Image.setMinimumSize(QSize(100, 100))
        self.day4Image.setMaximumSize(QSize(100, 100))
        self.day4Image.setScaledContents(True)
        self.day4Image.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day4Image, 1, 6, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.line_7 = QFrame(self.multiDay)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_37.addWidget(self.line_7, 1, 5, 1, 1)

        self.day5Info = QGridLayout()
        self.day5Info.setObjectName(u"day5Info")
        self.day5TempLow = QLabel(self.multiDay)
        self.day5TempLow.setObjectName(u"day5TempLow")

        self.day5Info.addWidget(self.day5TempLow, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.day5Desc = QLabel(self.multiDay)
        self.day5Desc.setObjectName(u"day5Desc")

        self.day5Info.addWidget(self.day5Desc, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.day5TempHi = QLabel(self.multiDay)
        self.day5TempHi.setObjectName(u"day5TempHi")

        self.day5Info.addWidget(self.day5TempHi, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.percipImage_13 = QLabel(self.multiDay)
        self.percipImage_13.setObjectName(u"percipImage_13")
        self.percipImage_13.setMinimumSize(QSize(30, 30))
        self.percipImage_13.setMaximumSize(QSize(30, 30))
        self.percipImage_13.setTextFormat(Qt.AutoText)
        self.percipImage_13.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_13.setScaledContents(True)
        self.percipImage_13.setAlignment(Qt.AlignCenter)
        self.percipImage_13.setIndent(0)

        self.day5Info.addWidget(self.percipImage_13, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_37.addLayout(self.day5Info, 2, 8, 1, 1)

        self.day4Date = QLabel(self.multiDay)
        self.day4Date.setObjectName(u"day4Date")
        self.day4Date.setMinimumSize(QSize(100, 15))
        self.day4Date.setMaximumSize(QSize(100, 15))
        self.day4Date.setFont(font3)
        self.day4Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day4Date, 0, 6, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.day2Image = QLabel(self.multiDay)
        self.day2Image.setObjectName(u"day2Image")
        self.day2Image.setMinimumSize(QSize(100, 100))
        self.day2Image.setMaximumSize(QSize(100, 100))
        self.day2Image.setScaledContents(True)
        self.day2Image.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day2Image, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.day1Image = QLabel(self.multiDay)
        self.day1Image.setObjectName(u"day1Image")
        self.day1Image.setMinimumSize(QSize(100, 100))
        self.day1Image.setMaximumSize(QSize(100, 100))
        self.day1Image.setScaledContents(True)
        self.day1Image.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day1Image, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.line_4 = QFrame(self.multiDay)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_37.addWidget(self.line_4, 1, 3, 1, 1)

        self.day5Image = QLabel(self.multiDay)
        self.day5Image.setObjectName(u"day5Image")
        self.day5Image.setMinimumSize(QSize(100, 100))
        self.day5Image.setMaximumSize(QSize(100, 100))
        self.day5Image.setScaledContents(True)
        self.day5Image.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day5Image, 1, 8, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.day3Info = QGridLayout()
        self.day3Info.setObjectName(u"day3Info")
        self.day3TempLow = QLabel(self.multiDay)
        self.day3TempLow.setObjectName(u"day3TempLow")

        self.day3Info.addWidget(self.day3TempLow, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.day3Desc = QLabel(self.multiDay)
        self.day3Desc.setObjectName(u"day3Desc")

        self.day3Info.addWidget(self.day3Desc, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.day3TempHi = QLabel(self.multiDay)
        self.day3TempHi.setObjectName(u"day3TempHi")

        self.day3Info.addWidget(self.day3TempHi, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.percipImage_6 = QLabel(self.multiDay)
        self.percipImage_6.setObjectName(u"percipImage_6")
        self.percipImage_6.setMinimumSize(QSize(30, 30))
        self.percipImage_6.setMaximumSize(QSize(30, 30))
        self.percipImage_6.setTextFormat(Qt.AutoText)
        self.percipImage_6.setPixmap(QPixmap(u"icons/raindrop.png"))
        self.percipImage_6.setScaledContents(True)
        self.percipImage_6.setAlignment(Qt.AlignCenter)
        self.percipImage_6.setIndent(0)

        self.day3Info.addWidget(self.percipImage_6, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_37.addLayout(self.day3Info, 2, 4, 1, 1)

        self.day6Date = QLabel(self.multiDay)
        self.day6Date.setObjectName(u"day6Date")
        self.day6Date.setMinimumSize(QSize(100, 15))
        self.day6Date.setMaximumSize(QSize(100, 15))
        self.day6Date.setFont(font3)
        self.day6Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day6Date, 0, 10, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.line_3 = QFrame(self.multiDay)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_37.addWidget(self.line_3, 1, 1, 1, 1)

        self.line_8 = QFrame(self.multiDay)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_37.addWidget(self.line_8, 1, 7, 1, 1)

        self.day6Image = QLabel(self.multiDay)
        self.day6Image.setObjectName(u"day6Image")
        self.day6Image.setMinimumSize(QSize(100, 100))
        self.day6Image.setMaximumSize(QSize(100, 100))
        self.day6Image.setScaledContents(True)
        self.day6Image.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day6Image, 1, 10, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.day5Date = QLabel(self.multiDay)
        self.day5Date.setObjectName(u"day5Date")
        self.day5Date.setMinimumSize(QSize(100, 15))
        self.day5Date.setMaximumSize(QSize(100, 15))
        self.day5Date.setFont(font3)
        self.day5Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day5Date, 0, 8, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.day3Image = QLabel(self.multiDay)
        self.day3Image.setObjectName(u"day3Image")
        self.day3Image.setMinimumSize(QSize(100, 100))
        self.day3Image.setMaximumSize(QSize(100, 100))
        self.day3Image.setScaledContents(True)
        self.day3Image.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.day3Image, 1, 4, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.line_9 = QFrame(self.multiDay)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_37.addWidget(self.line_9, 1, 9, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout_37)


        self.verticalLayout_31.addWidget(self.multiDay)

        self.muliDayScroll.setWidget(self.scrollAreaWidgetContents_10)

        self.gridMultipleDay_3.addWidget(self.muliDayScroll, 3, 0, 1, 1)

        self.line_17 = QFrame(self.frame_7)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(0, 1100, 551, 20))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.line_18 = QFrame(self.frame_7)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(0, 1550, 551, 20))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_3 = QWidget(self.frame_7)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 70, 781, 251))
        self.gridCurrent = QGridLayout(self.gridLayoutWidget_3)
        self.gridCurrent.setObjectName(u"gridCurrent")
        self.gridCurrent.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 2, 1)

        self.imageCurr = QLabel(self.gridLayoutWidget_3)
        self.imageCurr.setObjectName(u"imageCurr")
        self.imageCurr.setMaximumSize(QSize(150, 150))
        self.imageCurr.setMouseTracking(False)
        self.imageCurr.setScaledContents(True)
        self.imageCurr.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.imageCurr, 0, 3, 2, 1)

        self.tempLowCurr = QLabel(self.gridLayoutWidget_3)
        self.tempLowCurr.setObjectName(u"tempLowCurr")
        sizePolicy.setHeightForWidth(self.tempLowCurr.sizePolicy().hasHeightForWidth())
        self.tempLowCurr.setSizePolicy(sizePolicy)
        self.tempLowCurr.setFont(font3)
        self.tempLowCurr.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.tempLowCurr, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.tempCurr = QLabel(self.gridLayoutWidget_3)
        self.tempCurr.setObjectName(u"tempCurr")
        sizePolicy.setHeightForWidth(self.tempCurr.sizePolicy().hasHeightForWidth())
        self.tempCurr.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Geneva"])
        font4.setPointSize(48)
        self.tempCurr.setFont(font4)
        self.tempCurr.setAutoFillBackground(False)
        self.tempCurr.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.tempCurr, 0, 0, 2, 1)

        self.tempHighCurr = QLabel(self.gridLayoutWidget_3)
        self.tempHighCurr.setObjectName(u"tempHighCurr")
        sizePolicy.setHeightForWidth(self.tempHighCurr.sizePolicy().hasHeightForWidth())
        self.tempHighCurr.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"Geneva"])
        font5.setPointSize(18)
        font5.setBold(False)
        self.tempHighCurr.setFont(font5)
        self.tempHighCurr.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.tempHighCurr, 0, 1, 1, 1, Qt.AlignBottom)

        self.locationCurr = QLabel(self.gridLayoutWidget_3)
        self.locationCurr.setObjectName(u"locationCurr")
        font6 = QFont()
        font6.setFamilies([u"Geneva"])
        font6.setPointSize(24)
        self.locationCurr.setFont(font6)
        self.locationCurr.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.locationCurr, 0, 4, 2, 1)


        self.gridCurrent.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayoutWidget_14 = QWidget(self.frame_7)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(0, 1110, 541, 451))
        self.gridMetrics = QGridLayout(self.gridLayoutWidget_14)
        self.gridMetrics.setObjectName(u"gridMetrics")
        self.gridMetrics.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_80 = QLabel(self.gridLayoutWidget_14)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(75, 75))
        self.label_80.setPixmap(QPixmap(u"icons/aQual.png"))
        self.label_80.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_80, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.precipTotal = QLabel(self.gridLayoutWidget_14)
        self.precipTotal.setObjectName(u"precipTotal")
        self.precipTotal.setFont(font1)

        self.gridLayout_15.addWidget(self.precipTotal, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_82 = QLabel(self.gridLayoutWidget_14)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font2)
        self.label_82.setWordWrap(True)

        self.gridLayout_15.addWidget(self.label_82, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridMetrics.addLayout(self.gridLayout_15, 1, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_83 = QLabel(self.gridLayoutWidget_14)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMaximumSize(QSize(60, 60))
        self.label_83.setPixmap(QPixmap(u"icons/pressure.png"))
        self.label_83.setScaledContents(True)

        self.gridLayout_16.addWidget(self.label_83, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pressureVal = QLabel(self.gridLayoutWidget_14)
        self.pressureVal.setObjectName(u"pressureVal")
        self.pressureVal.setFont(font1)

        self.gridLayout_16.addWidget(self.pressureVal, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_77 = QLabel(self.gridLayoutWidget_14)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font2)
        self.label_77.setWordWrap(True)

        self.gridLayout_16.addWidget(self.label_77, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridMetrics.addLayout(self.gridLayout_16, 1, 2, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_85 = QLabel(self.gridLayoutWidget_14)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(75, 75))
        self.label_85.setPixmap(QPixmap(u"icons/windSpeed.png"))
        self.label_85.setScaledContents(True)

        self.gridLayout_17.addWidget(self.label_85, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.windSpeed = QLabel(self.gridLayoutWidget_14)
        self.windSpeed.setObjectName(u"windSpeed")
        self.windSpeed.setFont(font1)

        self.gridLayout_17.addWidget(self.windSpeed, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_87 = QLabel(self.gridLayoutWidget_14)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font2)
        self.label_87.setWordWrap(True)

        self.gridLayout_17.addWidget(self.label_87, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridMetrics.addLayout(self.gridLayout_17, 0, 2, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.airQual = QLabel(self.gridLayoutWidget_14)
        self.airQual.setObjectName(u"airQual")
        self.airQual.setFont(font1)

        self.gridLayout_14.addWidget(self.airQual, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_76 = QLabel(self.gridLayoutWidget_14)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font2)
        self.label_76.setWordWrap(True)

        self.gridLayout_14.addWidget(self.label_76, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_78 = QLabel(self.gridLayoutWidget_14)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(75, 75))
        self.label_78.setPixmap(QPixmap(u"icons/visibility.png"))
        self.label_78.setScaledContents(True)
        self.label_78.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_78, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridMetrics.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_88 = QLabel(self.gridLayoutWidget_14)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(60, 60))
        self.label_88.setPixmap(QPixmap(u"icons/humidityIndex.svg"))
        self.label_88.setScaledContents(True)

        self.gridLayout_18.addWidget(self.label_88, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.humidityIndex = QLabel(self.gridLayoutWidget_14)
        self.humidityIndex.setObjectName(u"humidityIndex")
        self.humidityIndex.setFont(font1)

        self.gridLayout_18.addWidget(self.humidityIndex, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_90 = QLabel(self.gridLayoutWidget_14)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font2)
        self.label_90.setWordWrap(True)

        self.gridLayout_18.addWidget(self.label_90, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridMetrics.addLayout(self.gridLayout_18, 1, 1, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_91 = QLabel(self.gridLayoutWidget_14)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMaximumSize(QSize(65, 65))
        self.label_91.setPixmap(QPixmap(u"icons/uvIndexIcon.webp"))
        self.label_91.setScaledContents(True)

        self.gridLayout_19.addWidget(self.label_91, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.uvIndex = QLabel(self.gridLayoutWidget_14)
        self.uvIndex.setObjectName(u"uvIndex")
        self.uvIndex.setFont(font1)

        self.gridLayout_19.addWidget(self.uvIndex, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_93 = QLabel(self.gridLayoutWidget_14)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font2)
        self.label_93.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_93, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridMetrics.addLayout(self.gridLayout_19, 0, 1, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.frame_7)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 1570, 531, 139))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.sunrise = QLabel(self.horizontalLayoutWidget_2)
        self.sunrise.setObjectName(u"sunrise")

        self.gridLayout_8.addWidget(self.sunrise, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_84 = QLabel(self.horizontalLayoutWidget_2)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMaximumSize(QSize(75, 75))
        self.label_84.setPixmap(QPixmap(u"icons/sunrise.png"))
        self.label_84.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_84, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_8)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sunset = QLabel(self.horizontalLayoutWidget_2)
        self.sunset.setObjectName(u"sunset")

        self.gridLayout_4.addWidget(self.sunset, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_81 = QLabel(self.horizontalLayoutWidget_2)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMaximumSize(QSize(75, 75))
        self.label_81.setPixmap(QPixmap(u"icons/sunset.png"))
        self.label_81.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_81, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_4)


        self.verticalLayout_22.addWidget(self.frame_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.gridLayoutWidget_2 = QWidget(self.Page2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(-10, 0, 621, 793))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(589, 779))
        self.label.setPixmap(QPixmap(u"images/Screenshot 2024-04-01 at 15.31.35.png"))
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.verticalLayoutWidget_4 = QWidget(self.Page3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 10, 591, 931))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.labelTitle_2 = QLabel(self.verticalLayoutWidget_4)
        self.labelTitle_2.setObjectName(u"labelTitle_2")
        font7 = QFont()
        font7.setFamilies([u"Geneva"])
        font7.setPointSize(24)
        font7.setBold(False)
        self.labelTitle_2.setFont(font7)
        self.labelTitle_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.labelTitle_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_3 = QScrollArea(self.verticalLayoutWidget_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 585, 887))
        self.layoutWidget_6 = QWidget(self.scrollAreaWidgetContents_7)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 0, 571, 81))
        self.gridLayout_24 = QGridLayout(self.layoutWidget_6)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.scienceButton_6 = QPushButton(self.layoutWidget_6)
        self.scienceButton_6.setObjectName(u"scienceButton_6")

        self.gridLayout_24.addWidget(self.scienceButton_6, 0, 1, 1, 1)

        self.spaceButton_6 = QPushButton(self.layoutWidget_6)
        self.spaceButton_6.setObjectName(u"spaceButton_6")

        self.gridLayout_24.addWidget(self.spaceButton_6, 0, 3, 1, 1)

        self.localButton_6 = QPushButton(self.layoutWidget_6)
        self.localButton_6.setObjectName(u"localButton_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.localButton_6.sizePolicy().hasHeightForWidth())
        self.localButton_6.setSizePolicy(sizePolicy1)

        self.gridLayout_24.addWidget(self.localButton_6, 0, 0, 1, 1)

        self.natureButton_6 = QPushButton(self.layoutWidget_6)
        self.natureButton_6.setObjectName(u"natureButton_6")

        self.gridLayout_24.addWidget(self.natureButton_6, 0, 2, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.scrollAreaWidgetContents_7)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 80, 591, 811))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(231, 151))
        self.label_4.setPixmap(QPixmap(u"newsImgs/ficke.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout_25.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(231, 151))
        self.label_3.setPixmap(QPixmap(u"newsImgs/solarEclipse.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout_25.addWidget(self.label_3, 2, 0, 1, 1)

        self.textEdit_21 = QTextEdit(self.gridLayoutWidget_6)
        self.textEdit_21.setObjectName(u"textEdit_21")
        sizePolicy.setHeightForWidth(self.textEdit_21.sizePolicy().hasHeightForWidth())
        self.textEdit_21.setSizePolicy(sizePolicy)
        self.textEdit_21.setMaximumSize(QSize(300, 151))

        self.gridLayout_25.addWidget(self.textEdit_21, 0, 1, 1, 1)

        self.textEdit_22 = QTextEdit(self.gridLayoutWidget_6)
        self.textEdit_22.setObjectName(u"textEdit_22")
        sizePolicy.setHeightForWidth(self.textEdit_22.sizePolicy().hasHeightForWidth())
        self.textEdit_22.setSizePolicy(sizePolicy)
        self.textEdit_22.setMaximumSize(QSize(300, 151))

        self.gridLayout_25.addWidget(self.textEdit_22, 2, 1, 1, 1)

        self.textEdit_23 = QTextEdit(self.gridLayoutWidget_6)
        self.textEdit_23.setObjectName(u"textEdit_23")
        sizePolicy.setHeightForWidth(self.textEdit_23.sizePolicy().hasHeightForWidth())
        self.textEdit_23.setSizePolicy(sizePolicy)
        self.textEdit_23.setMaximumSize(QSize(300, 151))

        self.gridLayout_25.addWidget(self.textEdit_23, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(231, 151))
        self.label_2.setPixmap(QPixmap(u"newsImgs/albertaFires.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_25.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(231, 151))
        self.label_5.setPixmap(QPixmap(u"newsImgs/springStorm.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_25.addWidget(self.label_5, 1, 0, 1, 1)

        self.textEdit_24 = QTextEdit(self.gridLayoutWidget_6)
        self.textEdit_24.setObjectName(u"textEdit_24")
        sizePolicy.setHeightForWidth(self.textEdit_24.sizePolicy().hasHeightForWidth())
        self.textEdit_24.setSizePolicy(sizePolicy)
        self.textEdit_24.setMaximumSize(QSize(300, 151))

        self.gridLayout_25.addWidget(self.textEdit_24, 3, 1, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_9.addWidget(self.scrollArea_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.stackedWidget.addWidget(self.Page3)
        self.Page4 = QWidget()
        self.Page4.setObjectName(u"Page4")
        self.verticalLayoutWidget_3 = QWidget(self.Page4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 10, 581, 771))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.verticalLayoutWidget_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(16777215, 750))
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 577, 748))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(16777215, 750))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 10, 431, 38))
        self.gridTitle = QGridLayout(self.gridLayoutWidget)
        self.gridTitle.setObjectName(u"gridTitle")
        self.gridTitle.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.gridLayoutWidget)
        self.labelTitle.setObjectName(u"labelTitle")
        font8 = QFont()
        font8.setFamilies([u"Geneva"])
        font8.setPointSize(16)
        font8.setBold(False)
        self.labelTitle.setFont(font8)
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridTitle.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.frame)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 60, 602, 251))
        self.gridProfile = QGridLayout(self.gridLayoutWidget_4)
        self.gridProfile.setObjectName(u"gridProfile")
        self.gridProfile.setHorizontalSpacing(2)
        self.gridProfile.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageProfile = QLabel(self.gridLayoutWidget_4)
        self.imageProfile.setObjectName(u"imageProfile")
        self.imageProfile.setMaximumSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.imageProfile)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelUsername = QLabel(self.gridLayoutWidget_4)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setAlignment(Qt.AlignCenter)
        self.labelUsername.setIndent(0)

        self.verticalLayout_6.addWidget(self.labelUsername)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBoxManageAccount = QComboBox(self.gridLayoutWidget_4)
        self.comboBoxManageAccount.addItem("")
        self.comboBoxManageAccount.addItem("")
        self.comboBoxManageAccount.addItem("")
        self.comboBoxManageAccount.addItem("")
        self.comboBoxManageAccount.addItem("")
        self.comboBoxManageAccount.setObjectName(u"comboBoxManageAccount")
        self.comboBoxManageAccount.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.comboBoxManageAccount, 0, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.buttonLogout = QPushButton(self.gridLayoutWidget_4)
        self.buttonLogout.setObjectName(u"buttonLogout")
        self.buttonLogout.setMinimumSize(QSize(0, 30))
        self.buttonLogout.setMaximumSize(QSize(60, 30))

        self.gridLayout_6.addWidget(self.buttonLogout, 0, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_6)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.gridProfile.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.frame)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 320, 551, 381))
        self.gridOtherSettings = QGridLayout(self.gridLayoutWidget_5)
        self.gridOtherSettings.setObjectName(u"gridOtherSettings")
        self.gridOtherSettings.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.gridLayoutWidget_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridOtherSettings.addWidget(self.line_2, 0, 0, 1, 1)

        self.verticalLayoutTime = QVBoxLayout()
        self.verticalLayoutTime.setObjectName(u"verticalLayoutTime")
        self.labelTime = QLabel(self.gridLayoutWidget_5)
        self.labelTime.setObjectName(u"labelTime")
        self.labelTime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayoutTime.addWidget(self.labelTime)

        self.radioButton12h = QRadioButton(self.gridLayoutWidget_5)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton12h)
        self.radioButton12h.setObjectName(u"radioButton12h")
        self.radioButton12h.setChecked(True)

        self.verticalLayoutTime.addWidget(self.radioButton12h)

        self.radioButton24h = QRadioButton(self.gridLayoutWidget_5)
        self.buttonGroup.addButton(self.radioButton24h)
        self.radioButton24h.setObjectName(u"radioButton24h")

        self.verticalLayoutTime.addWidget(self.radioButton24h)


        self.gridOtherSettings.addLayout(self.verticalLayoutTime, 2, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridOtherSettings.addWidget(self.line, 4, 0, 2, 1)

        self.verticalLayoutUnits = QVBoxLayout()
        self.verticalLayoutUnits.setObjectName(u"verticalLayoutUnits")
        self.labelUnits = QLabel(self.gridLayoutWidget_5)
        self.labelUnits.setObjectName(u"labelUnits")
        self.labelUnits.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayoutUnits.addWidget(self.labelUnits)

        self.radioButtonMetric = QRadioButton(self.gridLayoutWidget_5)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButtonMetric)
        self.radioButtonMetric.setObjectName(u"radioButtonMetric")

        self.verticalLayoutUnits.addWidget(self.radioButtonMetric)

        self.radioButtonImperial = QRadioButton(self.gridLayoutWidget_5)
        self.buttonGroup_2.addButton(self.radioButtonImperial)
        self.radioButtonImperial.setObjectName(u"radioButtonImperial")
        self.radioButtonImperial.setChecked(True)

        self.verticalLayoutUnits.addWidget(self.radioButtonImperial)


        self.gridOtherSettings.addLayout(self.verticalLayoutUnits, 1, 0, 1, 1)

        self.verticalLayoutLang = QVBoxLayout()
        self.verticalLayoutLang.setObjectName(u"verticalLayoutLang")
        self.labelLang = QLabel(self.gridLayoutWidget_5)
        self.labelLang.setObjectName(u"labelLang")

        self.verticalLayoutLang.addWidget(self.labelLang)

        self.comboBoxLang = QComboBox(self.gridLayoutWidget_5)
        self.comboBoxLang.addItem("")
        self.comboBoxLang.addItem("")
        self.comboBoxLang.addItem("")
        self.comboBoxLang.setObjectName(u"comboBoxLang")

        self.verticalLayoutLang.addWidget(self.comboBoxLang)


        self.gridOtherSettings.addLayout(self.verticalLayoutLang, 3, 0, 1, 1)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(0, 720, 551, 101))
        self.label_35.setFont(font2)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(0, 1100, 551, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_21 = QWidget(self.frame)
        self.gridLayoutWidget_21.setObjectName(u"gridLayoutWidget_21")
        self.gridLayoutWidget_21.setGeometry(QRect(0, 1580, 158, 88))
        self.verticalLayout_5 = QVBoxLayout(self.gridLayoutWidget_21)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.gridLayoutWidget_21)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout_5.addWidget(self.label_73)

        self.label_74 = QLabel(self.gridLayoutWidget_21)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_5.addWidget(self.label_74)

        self.label_72 = QLabel(self.gridLayoutWidget_21)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_5.addWidget(self.label_72)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 1550, 551, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.frame)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.Page4)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.verticalWidget = QWidget(self.verticalLayoutWidget_2)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.verticalWidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.home_btn = QPushButton(self.widget)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy1.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"icons/home_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.home_btn, 1, 0, 1, 1)

        self.radar_btn = QPushButton(self.widget)
        self.radar_btn.setObjectName(u"radar_btn")
        icon1 = QIcon()
        icon1.addFile(u"icons/radar_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radar_btn.setIcon(icon1)
        self.radar_btn.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.radar_btn, 1, 1, 1, 1)

        self.sett_btn = QPushButton(self.widget)
        self.sett_btn.setObjectName(u"sett_btn")
        icon2 = QIcon()
        icon2.addFile(u"icons/settings_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sett_btn.setIcon(icon2)
        self.sett_btn.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.sett_btn, 1, 3, 1, 1)

        self.news_btn = QPushButton(self.widget)
        self.news_btn.setObjectName(u"news_btn")
        icon3 = QIcon()
        icon3.addFile(u"icons/news_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.news_btn.setIcon(icon3)
        self.news_btn.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.news_btn, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.verticalWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 607, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_entry.setText("")
        self.search_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for a location...", None))
        self.time_3.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.temp_3.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.image_3.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.percipImage_8.setText("")
        self.percipPer_3.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.time_6.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.temp_6.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.image_6.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.percipImage_11.setText("")
        self.percipPer_6.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.time_5.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.temp_5.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.image_5.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.percipImage_10.setText("")
        self.percipPer_5.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.time_7.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.temp_7.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.image_7.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.percipImage_12.setText("")
        self.percipPer_7.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.time_2.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.temp_2.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.image_2.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.percipImage_2.setText("")
        self.percipPer_2.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.time_4.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.temp_4.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.image_4.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.percipImage_9.setText("")
        self.percipPer_4.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.time_1.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.temp_1.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.image_1.setText(QCoreApplication.translate("MainWindow", u"weatherImage", None))
        self.percipImage_1.setText("")
        self.percipPer_1.setText(QCoreApplication.translate("MainWindow", u"precipitationPercent", None))
        self.hourlyLabel.setText(QCoreApplication.translate("MainWindow", u"Hourly Forecast", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"\u2308AD CONTAINER\u230b", None))
        self.chooseDay.setItemText(0, QCoreApplication.translate("MainWindow", u"7-Day Forecast", None))
        self.chooseDay.setItemText(1, QCoreApplication.translate("MainWindow", u"3-Day Forecast", None))
        self.chooseDay.setItemText(2, QCoreApplication.translate("MainWindow", u"14-Day Forecast", None))

        self.chooseDay.setCurrentText("")
        self.chooseDay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Days", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"Weather Forecast", None))
        self.day2Date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.day2TempLow.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.day2Desc.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.day2TempHi.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.percipImage_5.setText("")
        self.day4TempLow.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.day4Desc.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.day4TempHi.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.percipImage_7.setText("")
        self.day6TempLow.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.day6Desc.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.day6TempHi.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.percipImage_14.setText("")
        self.day1Date.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.day3Date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.day1TempLow.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.day1Desc.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.day1TempHi.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.percipImage_3.setText("")
        self.day4Image.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.day5TempLow.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.day5Desc.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.day5TempHi.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.percipImage_13.setText("")
        self.day4Date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.day2Image.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.day1Image.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.day5Image.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.day3TempLow.setText(QCoreApplication.translate("MainWindow", u"TempLow", None))
        self.day3Desc.setText(QCoreApplication.translate("MainWindow", u"WDescrip", None))
        self.day3TempHi.setText(QCoreApplication.translate("MainWindow", u"TempHigh", None))
        self.percipImage_6.setText("")
        self.day6Date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.day6Image.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.day5Date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.day3Image.setText(QCoreApplication.translate("MainWindow", u"Date/Day", None))
        self.imageCurr.setText(QCoreApplication.translate("MainWindow", u"Wimage", None))
        self.tempLowCurr.setText(QCoreApplication.translate("MainWindow", u"TempLowDay", None))
        self.tempCurr.setText("")
        self.tempHighCurr.setText(QCoreApplication.translate("MainWindow", u"TempHighDay", None))
        self.locationCurr.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_80.setText("")
        self.precipTotal.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Precipitation", None))
        self.label_83.setText("")
        self.pressureVal.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.label_85.setText("")
        self.windSpeed.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Wind", None))
        self.airQual.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Visibility", None))
        self.label_78.setText("")
        self.label_88.setText("")
        self.humidityIndex.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.label_91.setText("")
        self.uvIndex.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"UV-Index", None))
        self.sunrise.setText(QCoreApplication.translate("MainWindow", u"Sunrise Time", None))
        self.label_84.setText("")
        self.sunset.setText(QCoreApplication.translate("MainWindow", u"Sunset Time", None))
        self.label_81.setText("")
        self.label.setText("")
        self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"News", None))
        self.scienceButton_6.setText(QCoreApplication.translate("MainWindow", u"Science", None))
        self.spaceButton_6.setText(QCoreApplication.translate("MainWindow", u"Space", None))
        self.localButton_6.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.natureButton_6.setText(QCoreApplication.translate("MainWindow", u"Nature", None))
        self.label_4.setText("")
        self.label_3.setText("")
        self.textEdit_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Geneva'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue'; font-size:18pt;\">Alberta wildfire season is off to a blazing start, 57 fires burning</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue';\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue';\">With the 2024 wildfire season heavily looming over the backs of Canadians after last year\u2019s historic wildfire season, none will be feeling the pressure more than Western Canada.\u00a0</span><a href=\"https://www.theweathernetwork.com/en/news/weather/severe/whats-the-recipe-for-a-severe-drought-in-western-canada\"><span style=\" font-family:'Helvetica Neue'; text-decoration: underline; color:#094fd1;\">Widespread drought</span></a><span style=\" font-family:'Helvetica Neue';\">, low snow-pack levels, and warm temperatures have many people fearing for what this season will bring.\u00a0</span><span style=\" font-family:'.AppleSystemUIFont';\"> </span></p></body></html>", None))
        self.textEdit_22.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Geneva'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue'; font-size:18pt;\">April 8 solar eclipse is a must-see celestial event this spring</span><span style=\" font-family:'Helvetica Neue';\"><br /></span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica Neue';\"><br /></p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue';\">In addition to the bright planets and meteor showers visible throughout the spring season, a 'once-in-a-lifetime' solar eclipse will darken our daytime sky on April 8. \u00a0 On March 19, at precisely 11:06 p.m. EDT, the Sun will cross the celestial equator from south to north, signifying the\u00a0 [earliest start to spring in 128 years].</span></p></body></html>", None))
        self.textEdit_23.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Geneva'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue'; font-size:18pt;\">Potent spring storm setup threatens heavy snow over parts of Quebec</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue';\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue';\">A dynamic storm system is forecast to sweep across Quebec this week, bringing with it the potential for rain, gusty winds, and heavy snow. Travel disruptions and power outages are possible\u00a0 \u00a0</span><span style=\" font-family:'.AppleSystemUIFont';\"> </span></p></body></html>", None))
        self.label_2.setText("")
        self.label_5.setText("")
        self.textEdit_24.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Geneva'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue'; font-size:18pt;\">Canada faces a fickle April as winter wanes and summer teases</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue';\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue';\">April can be such a fickle month! While the middle of spring is notorious for delivering\u00a0 [parting shots from winter](https://www.theweathernetwork.com/en/news/weather/forecasts/reality-check-april-is-never-really-that-nice-canada) , it\u2019ll also tease us with brief tastes of summer-like warmth from time to time. Sometimes, we\u2019ll see both within a few days!\u00a0 \u00a0</span><span style=\" font-family:'.AppleSystemUIFont';\"> </span></p></body></html>", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.imageProfile.setText(QCoreApplication.translate("MainWindow", u"Profile Image", None))
        self.labelUsername.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.comboBoxManageAccount.setItemText(0, QCoreApplication.translate("MainWindow", u"Manage", None))
        self.comboBoxManageAccount.setItemText(1, QCoreApplication.translate("MainWindow", u"Profile", None))
        self.comboBoxManageAccount.setItemText(2, QCoreApplication.translate("MainWindow", u"Uploads", None))
        self.comboBoxManageAccount.setItemText(3, QCoreApplication.translate("MainWindow", u"Edit Locations", None))
        self.comboBoxManageAccount.setItemText(4, QCoreApplication.translate("MainWindow", u"Alerts", None))

        self.buttonLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.labelTime.setText(QCoreApplication.translate("MainWindow", u"Time Format", None))
        self.radioButton12h.setText(QCoreApplication.translate("MainWindow", u"12-hour", None))
        self.radioButton24h.setText(QCoreApplication.translate("MainWindow", u"24-hour", None))
        self.labelUnits.setText(QCoreApplication.translate("MainWindow", u"Units", None))
        self.radioButtonMetric.setText(QCoreApplication.translate("MainWindow", u"Metric (mph/ \u00b0F)", None))
        self.radioButtonImperial.setText(QCoreApplication.translate("MainWindow", u"Imperial (km/h / \u00b0C)", None))
        self.labelLang.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.comboBoxLang.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBoxLang.setItemText(1, QCoreApplication.translate("MainWindow", u"French", None))
        self.comboBoxLang.setItemText(2, QCoreApplication.translate("MainWindow", u"Spanish", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ad Container", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Sunrise/Sunset Icon", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Sunrise Time", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Sunset Time", None))
        self.home_btn.setText("")
        self.radar_btn.setText("")
        self.sett_btn.setText("")
        self.news_btn.setText("")
    # retranslateUi

