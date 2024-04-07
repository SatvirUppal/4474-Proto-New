# This Python file uses the following encoding: utf-8
import sys


from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui, QtCore
from datetime import datetime, timedelta

from Location import Location

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#from ui_form import Ui_MainWindow
from ui_homepage import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.frame_7.setEnabled(False)

        self.ui.search_entry.setFocus()

        self.ui.search_btn.clicked.connect(self.getWeatherData)

        self.ui.stackedWidget.setCurrentWidget(self.ui.Page1)

        self.ui.home_btn.clicked.connect(self.getWeatherData)
        self.ui.radar_btn.clicked.connect(self.showPage2)
        self.ui.news_btn.clicked.connect(self.showPage3)
        self.ui.sett_btn.clicked.connect(self.showPage4)

        self.ui.radioButton12h.toggled.connect(self.setHourUnits)
        self.ui.radioButtonImperial.toggled.connect(self.setUnits)

        self.hour12 = True
        self.imperial = True

    def setHourUnits(self):
        if(self.ui.radioButton12h.isChecked()):
            self.hour12 = True
        else:
            self.hour12 = False

    def setUnits(self):
        if(self.ui.radioButtonImperial.isChecked()):
            self.imperial = True
        else:
            self.imperial = False 

    def showPage1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Page1)
        print(self.hour12)
    def showPage2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Page2)
    def showPage3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Page3)
    def showPage4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Page4)


    def __tempFormat(self,temp):
        if(self.imperial):
            return (str(temp) + "°C")
        else:
            return (str(int((temp* 9/5) + 32)) + "°F")
    
    def __hourFormat(self):
        if (self.hour12):
            return "%I %p"
        else:
            return "%H"


    def getWeatherData(self):
        loc = self.ui.search_entry.text()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Page1)

        if (loc == ""):
            return 0
        
        self.ui.frame_7.setEnabled(True)
        self.ui.frame_8.setEnabled(True)
        self.ui.hourlyTimeLine.setEnabled(True)
        self.ui.scrollAreaWidgetContents_9.setEnabled(True)

        self.ui.centralwidget.setEnabled(True)

        # Get Data to fill Current Forecast Box
        locData = Location(loc)
        self.ui.tempCurr.setText(self.__tempFormat(locData.getTemperature()))
        self.ui.tempHighCurr.setText(self.__tempFormat(locData.getMaxTempCelc()))
        
        self.ui.tempLowCurr.setText(self.__tempFormat(locData.getMinTempCelc()))
        self.ui.imageCurr.setText("")
        currWeather = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName()) + ".png")
        self.ui.imageCurr.setPixmap(currWeather)
        self.ui.locationCurr.setText(loc)

        ### Hourly Time Stamping
        
        # Hour 1
        nextTime = datetime.now() + timedelta(hours = 1)
        self.ui.time_1.setText(nextTime.strftime(self.__hourFormat()))
        self.ui.image_1.setText("")
        hourly = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(1)) + ".png")
        self.ui.image_1.setPixmap(hourly)
        self.ui.temp_1.setText(self.__tempFormat(locData.getTemperature(1)))
        self.ui.percipPer_1.setText(str(locData.getPrecChance(1))+ "%")

        # Hour 2
        nextTime = datetime.now() + timedelta(hours = 2)
        self.ui.time_2.setText(nextTime.strftime(self.__hourFormat()))
        self.ui.image_2.setText("")
        hourly = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(2)) + ".png")
        self.ui.image_2.setPixmap(hourly)
        self.ui.temp_2.setText(self.__tempFormat(locData.getTemperature(2)))
        self.ui.percipPer_2.setText(str(locData.getPrecChance(2))+ "%")
        
        # Hour 3
        nextTime = datetime.now() + timedelta(hours = 3)
        self.ui.time_3.setText(nextTime.strftime(self.__hourFormat()))
        self.ui.image_3.setText("")
        hourly = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(3)) + ".png")
        self.ui.image_3.setPixmap(hourly)
        self.ui.temp_3.setText(self.__tempFormat(locData.getTemperature(3)))
        self.ui.percipPer_3.setText(str(locData.getPrecChance(3))+ "%")

        # Hour 4
        nextTime = datetime.now() + timedelta(hours = 4)
        self.ui.time_4.setText(nextTime.strftime(self.__hourFormat()))
        self.ui.image_4.setText("")
        hourly = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(4)) + ".png")
        self.ui.image_4.setPixmap(hourly)
        self.ui.temp_4.setText(self.__tempFormat(locData.getTemperature(4)))
        self.ui.percipPer_4.setText(str(locData.getPrecChance(4))+ "%")

        # Hour 5
        nextTime = datetime.now() + timedelta(hours = 5)
        self.ui.time_5.setText(nextTime.strftime(self.__hourFormat()))
        self.ui.image_5.setText("")
        hourly = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(5)) + ".png")
        self.ui.image_5.setPixmap(hourly)
        self.ui.temp_5.setText(self.__tempFormat(locData.getTemperature(5)))
        self.ui.percipPer_5.setText(str(locData.getPrecChance(5))+ "%")

        # Hour 6
        nextTime = datetime.now() + timedelta(hours = 6)
        self.ui.time_6.setText(nextTime.strftime(self.__hourFormat()))
        self.ui.image_6.setText("")
        hourly = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(6)) + ".png")
        self.ui.image_6.setPixmap(hourly)
        self.ui.temp_6.setText(self.__tempFormat(locData.getTemperature(6)))
        self.ui.percipPer_6.setText(str(locData.getPrecChance(6))+ "%")

        # Hour 7
        nextTime = datetime.now() + timedelta(hours = 7)
        self.ui.time_7.setText(nextTime.strftime(self.__hourFormat()))
        self.ui.image_7.setText("")
        hourly = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(7)) + ".png")
        self.ui.image_7.setPixmap(hourly)
        self.ui.temp_7.setText(self.__tempFormat(locData.getTemperature(7)))
        self.ui.percipPer_7.setText(str(locData.getPrecChance(7))+ "%")

        ###----------------------------------------------------------------------------------
        ### Daily Update: 
        now = datetime.now()
    
        # Calculate the datetime for noon tomorrow
        noon_tomorrow = (now + timedelta(days=1)).replace(hour=12, minute=0, second=0, microsecond=0)
        
        # Calculate the difference in hours
        difference = noon_tomorrow - now
        hours_difference = int(difference.total_seconds() // 3600)
        
        ## +1 Day
        nextDay = datetime.now() + timedelta(days=1)
        self.ui.day1Date.setText(nextDay.strftime('%m/%d'))
        self.ui.day1Image.setText("")
        daily = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(hours_difference)) + ".png")
        self.ui.day1Image.setPixmap(daily)
        self.ui.day1TempHi.setText(self.__tempFormat(locData.getMaxTempCelc(hours_difference)))
        self.ui.day1TempLow.setText(self.__tempFormat(locData.getMinTempCelc(hours_difference)))
        self.ui.day1Desc.setText(str(locData.getPrecChance(hours_difference))+"%")
        
        ## +2 Day
        # add another 24 to account for the follwing day
        hours_difference += 24
        nextDay += timedelta(days=1)
        self.ui.day2Date.setText(nextDay.strftime('%m/%d'))
        self.ui.day2Image.setText("")
        daily = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(hours_difference)) + ".png")
        self.ui.day2Image.setPixmap(daily)
        self.ui.day2TempHi.setText(self.__tempFormat(locData.getMaxTempCelc(hours_difference)))
        self.ui.day2TempLow.setText(self.__tempFormat(locData.getMinTempCelc(hours_difference)))
        self.ui.day2Desc.setText(str(locData.getPrecChance(hours_difference))+"%")

        ## +3 Day
        # add another 24 to account for the follwing day
        hours_difference += 24
        nextDay += timedelta(days=1)
        self.ui.day3Date.setText(nextDay.strftime('%m/%d'))
        self.ui.day3Image.setText("")
        daily = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(hours_difference)) + ".png")
        self.ui.day3Image.setPixmap(daily)
        self.ui.day3TempHi.setText(self.__tempFormat(locData.getMaxTempCelc(hours_difference)))
        self.ui.day3TempLow.setText(self.__tempFormat(locData.getMinTempCelc(hours_difference)))
        self.ui.day3Desc.setText(str(locData.getPrecChance(hours_difference))+"%")

        ## +4 Day
        # add another 24 to account for the follwing day
        hours_difference += 24
        nextDay += timedelta(days=1)
        self.ui.day4Date.setText(nextDay.strftime('%m/%d'))
        self.ui.day4Image.setText("")
        daily = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(hours_difference)) + ".png")
        self.ui.day4Image.setPixmap(daily)
        self.ui.day4TempHi.setText(self.__tempFormat(locData.getMaxTempCelc(hours_difference)))
        self.ui.day4TempLow.setText(self.__tempFormat(locData.getMinTempCelc(hours_difference)))
        self.ui.day4Desc.setText(str(locData.getPrecChance(hours_difference))+"%")

        ## +5 Day
        # add another 24 to account for the follwing day
        hours_difference += 24
        nextDay += timedelta(days=1)
        self.ui.day5Date.setText(nextDay.strftime('%m/%d'))
        self.ui.day5Image.setText("")
        daily = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(hours_difference)) + ".png")
        self.ui.day5Image.setPixmap(daily)
        self.ui.day5TempHi.setText(self.__tempFormat(locData.getMaxTempCelc(hours_difference)))
        self.ui.day5TempLow.setText(self.__tempFormat(locData.getMinTempCelc(hours_difference)))
        self.ui.day5Desc.setText(str(locData.getPrecChance(hours_difference))+"%")

        ## +6 Day
        # add another 24 to account for the follwing day
        hours_difference += 24
        nextDay += timedelta(days=1)
        self.ui.day6Date.setText(nextDay.strftime('%m/%d'))
        self.ui.day6Image.setText("")
        daily = QtGui.QPixmap("weatherIcons/" + str(locData.getIconName(hours_difference)) + ".png")
        self.ui.day6Image.setPixmap(daily)
        self.ui.day6TempHi.setText(self.__tempFormat(locData.getMaxTempCelc(hours_difference)))
        self.ui.day6TempLow.setText(self.__tempFormat(locData.getMinTempCelc(hours_difference)))
        self.ui.day6Desc.setText(str(locData.getPrecChance(hours_difference))+"%")

        ###---------------------------------------------------------------------------------------------
        ### Metrics 

        uv = locData.getUVIndex()
        if (uv == 0):
            self.ui.uvIndex.setText("-")
        else:
            self.ui.uvIndex.setText(str(uv))
        print("Metrics: ")
        print(self.imperial)
        self.setUnits()
        print(self.imperial)
        if(self.imperial):
            self.ui.airQual.setText(str(locData.getVisibility()/1000) + "km")
            self.ui.windSpeed.setText(str(locData.getWindSpeed()) + " km/h °" + str(locData.getWindDirection()))
            self.ui.precipTotal.setText(str(locData.getPrecipitationTotal()) + " mm")
            self.ui.pressureVal.setText(str(int((locData.getSurfacePressure()/1000)*101.3)) + " KPa")
        else:
            self.ui.airQual.setText(str(round(locData.getVisibility()/1609, 1)) + " mi")
            self.ui.windSpeed.setText(str(round(locData.getWindSpeed()/1.609, 1)) + " mph °" + str(locData.getWindDirection()))
            self.ui.precipTotal.setText(str(round(locData.getPrecipitationTotal()/25.4, 2)) + " in")
            self.ui.pressureVal.setText(str(round((locData.getSurfacePressure()/1000)*101.3/6.895, 2)) + " PSI")

        self.ui.humidityIndex.setText(str(locData.getHumidity()) + "%")

        ###----------------------------------------------------------------------------------------------
        ### Sunet Times - Non functioning due to API -> Values are faked
        # self.ui.sunrise.setText(str(locData.getSunriseTime()))
        # self.ui.sunset.setText(str(locData.getSunsetTime()))
        if (self.hour12):
            self.ui.sunrise.setText("6:42 AM")
            self.ui.sunset.setText("7:15 PM")
        else: 
            self.ui.sunrise.setText("06:42")
            self.ui.sunset.setText("18:15")

        self.ui.Page1.update()
        QApplication.processEvents()
        return 0;
    
# TEST TEST TEST TEST

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
