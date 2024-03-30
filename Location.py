import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry


class Location:

    def __init__(self, latitude, longitude, name):
        self._latitude = latitude
        self._longitude = longitude
        self._name = name

        # hourly info list
        self._tempCelc = None
        self._humidity = None
        self._precChance = None
        self._weatherCode = None
        self._surfacePressure = None
        self._visibility = None
        self._windSpeed = None
        self._windDirection = None
        self._uvIndex = None
        self._dateList = None

        # daily info list
        self._sunriseTime = None
        self._sunsetTime = None
        self._precipitationTotal = None
        self._maxTempCelc = None
        self._minTempCelc = None

        self.refresh_data()

    def refresh_data(self):
        hourlyData, dailyData = self._weather_Info_Call()

        # set sets of hourly data
        # all are pd series
        self._tempCelc = hourlyData["temperature_2m"]
        self._humidity = hourlyData["relative_humidity_2m"]
        self._precChance = hourlyData["precipitation_probability"]
        self._weatherCode = hourlyData["weather_code"]
        self._surfacePressure = hourlyData["surface_pressure"]
        self._visibility = hourlyData["visibility"]
        self._windSpeed = hourlyData["wind_speed_10m"]
        self._windDirection = hourlyData["wind_direction_10m"]
        self._uvIndex = hourlyData["uv_index"]
        self._dateList = hourlyData["date"]

        # set sets of daily data
        # all are pd series
        self._sunriseTime = dailyData["sunrise"]
        self._sunsetTime = dailyData["sunset"]
        self._precipitationTotal = dailyData["precipitation_sum"]
        self._maxTempCelc = dailyData["temperature_2m_max"]
        self._minTempCelc = dailyData["temperature_2m_min"]

        # set sets of hourly data
        # all are pd series
        # self._tempCelc = hourlyData["temperature_2m"]
        # print("\n_tempCelc\n", self._tempCelc)
        #
        # self._humidity = hourlyData["relative_humidity_2m"]
        # print("\n_humidity\n", self._humidity)
        #
        # self._precChance = hourlyData["precipitation_probability"]
        # print("\n_precChance\n", self._precChance)
        #
        # self._weatherCode = hourlyData["weather_code"]
        # print("\n_weatherCode\n", self._weatherCode)
        #
        # self._surfacePressure = hourlyData["surface_pressure"]
        # print("\n_surfacePressure\n", self._surfacePressure)
        #
        # self._visibility = hourlyData["visibility"]
        # print("\n_visibility\n", self._visibility)
        #
        # self._windSpeed = hourlyData["wind_speed_10m"]
        # print("\n_windSpeed\n", self._windSpeed)
        #
        # self._windDirection = hourlyData["wind_direction_10m"]
        # print("\n_windDirection\n", self._windDirection)
        #
        # self._uvIndex = hourlyData["uv_index"]
        # print("\n_uvIndex\n", self._uvIndex)
        #
        # # set sets of daily data
        # # all are pd series
        # self._sunsetTime = dailyData["sunset"]
        # print("\n_sunsetTime\n", self._sunsetTime)
        #
        # self._sunriseTime = dailyData["sunrise"]
        # print("\n_sunsetTime\n", self._sunsetTime)
        #
        # self._precipitationTotal = dailyData["precipitation_sum"]
        # print("\n_precipitationTotal\n", self._precipitationTotal)
        #
        # self._maxTempCelc = dailyData["temperature_2m_max"]
        # print("\n_maxTempCelc\n", self._maxTempCelc)
        #
        # self._minTempCelc = dailyData["temperature_2m_min"]
        # print("\n_minTempCelc\n", self._minTempCelc)

    def _weather_Info_Call(self):
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation_probability", "weather_code",
                       "surface_pressure", "visibility", "wind_speed_10m", "wind_direction_10m", "uv_index"],
            "daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "precipitation_sum"],
            "timezone": "America/New_York"
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
        hourly_precipitation_probability = hourly.Variables(2).ValuesAsNumpy()
        hourly_weather_code = hourly.Variables(3).ValuesAsNumpy()
        hourly_surface_pressure = hourly.Variables(4).ValuesAsNumpy()
        hourly_visibility = hourly.Variables(5).ValuesAsNumpy()
        hourly_wind_speed_10m = hourly.Variables(6).ValuesAsNumpy()
        hourly_wind_direction_10m = hourly.Variables(7).ValuesAsNumpy()
        hourly_uv_index = hourly.Variables(8).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )}
        hourly_data["temperature_2m"] = hourly_temperature_2m
        hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
        hourly_data["precipitation_probability"] = hourly_precipitation_probability
        hourly_data["weather_code"] = hourly_weather_code
        hourly_data["surface_pressure"] = hourly_surface_pressure
        hourly_data["visibility"] = hourly_visibility
        hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
        hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
        hourly_data["uv_index"] = hourly_uv_index

        hourly_dataframe = pd.DataFrame(data=hourly_data)
        print(hourly_dataframe)

        # Process daily data. The order of variables needs to be the same as requested.
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
        daily_sunrise = daily.Variables(2).ValuesAsNumpy()
        daily_sunset = daily.Variables(3).ValuesAsNumpy()
        daily_precipitation_sum = daily.Variables(4).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )}
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min
        daily_data["sunrise"] = daily_sunrise
        daily_data["sunset"] = daily_sunset
        daily_data["precipitation_sum"] = daily_precipitation_sum

        daily_dataframe = pd.DataFrame(data=daily_data)
        print(daily_dataframe)

        return hourly_dataframe, daily_dataframe

    """
    HOURLY GETTERS
    """

    def getTemperature(self, offset=0):
        return round(self._tempCelc.iloc[offset])

    def getHumidity(self, offset=0):
        return round(self._humidity.iloc[offset])

    def getPrecChance(self, offset=0):
        return round(self._precChance.iloc[offset])

    def getWeatherCode(self, offset=0):
        return self._weatherCode.iloc[offset]

    def getWeatherName(self, offset=0):
        weather_mapping = {
            0: "Clear Sky",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing Rime Fog",
            51: "Light Drizzle",
            53: "Moderate Drizzle",
            55: "Dense Drizzle",
            56: "Light Freezing Drizzle",
            57: "Dense Freezing Drizzle",
            61: "Slight Rain",
            63: "Moderate Rain",
            65: "Heavy Rain",
            66: "Light Freezing Rain",
            67: "Heavy Freezing Rain",
            71: "Slight Snow",
            73: "Moderate Snow",
            75: "Heavy Snow",
            77: "Snow Grains",
            80: "Slight Rain Showers",
            81: "Moderate Rain Showers",
            82: "Heavy Rain Showers",
            85: "Slight Snow Showers",
            86: "Heavy Snow Showers",
            95: "Thunderstorm"
        }

        return weather_mapping.get(self._weatherCode.iloc[offset])

    def getSurfacePressure(self, offset=0):
        return round(self._surfacePressure.iloc[offset])

    def getVisibility(self, offset=0):
        return round(self._visibility.iloc[offset])

    def getWindSpeed(self, offset=0):
        return round(self._windSpeed.iloc[offset])

    def getWindDirection(self, offset=0):
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']  # define directions possible
        # add 22.5 (half 45, and divide by range of each section)
        return directions[int((self._windDirection.iloc[offset] + 22.5) // 45)]

    def getUVIndex(self, offset=0):
        return round(self._uvIndex.iloc[offset])

    def getIconName(self, offset=0):
        datetime_pd = pd.Timestamp(self._dateList.iloc[offset])

        morningStart = datetime_pd.replace(hour=7, minute=0, second=0, microsecond=0)
        eveningStart = datetime_pd.replace(hour=20, minute=0, second=0, microsecond=0)

        if morningStart <= datetime_pd < eveningStart:
            weatherIconMap = {
                0: "00-ClearSkyDay",
                1: "0102-ClearCloudyDay",
                2: "0102-ClearCloudyDay",
                3: "03-Overcast",
                45: "45-Fog",
                48: "45-Fog",
                51: "5153-DrizzleDay",
                53: "5153-DrizzleDay",
                55: "5561-DrizzleRain",
                56: "5561-DrizzleRain",
                57: "5561-DrizzleRain",
                61: "5561-DrizzleRain",
                63: "63-Rain",
                65: "65-Rain",
                66: "63-Rain",
                67: "65-Rain",
                71: "717375-Snow",
                73: "717375-Snow",
                75: "717375-Snow",
                77: "717375-Snow",
                80: "5153-DrizzleDay",
                81: "5153-DrizzleDay",
                82: "5153-DrizzleDay",
                85: "8586-SnowDay",
                86: "8586-SnowDay",
                95: "95-Thunderstorm"
            }
        else:
            weatherIconMap = {
                0: "00-ClearSkyNight",
                1: "0102-ClearCloudyNight",
                2: "0102-ClearCloudyNight",
                3: "03-Overcast",
                45: "45-Fog",
                48: "45-Fog",
                51: "5153-DrizzleNight",
                53: "5153-DrizzleNight",
                55: "5561-DrizzleRain",
                56: "5561-DrizzleRain",
                57: "5561-DrizzleRain",
                61: "5561-DrizzleRain",
                63: "63-Rain",
                65: "65-Rain",
                66: "63-Rain",
                67: "65-Rain",
                71: "717375-Snow",
                73: "717375-Snow",
                75: "717375-Snow",
                77: "717375-Snow",
                80: "5153-DrizzleNight",
                81: "5153-DrizzleNight",
                82: "5153-DrizzleNight",
                85: "8586-SnowNight",
                86: "8586-SnowNight",
                95: "95-Thunderstorm"
            }
        return weatherIconMap.get(self._weatherCode.iloc[offset])



    """
    DAILY GETTERS: All offsets are divided by 24 and rounded down
    """

    def getSunriseTime(self, offset=0):
        return self._sunriseTime.iloc[offset//24]

    def getSunsetTime(self, offset=0):
        return self._sunsetTime.iloc[offset//24]

    def getPrecipitationTotal(self, offset=0):
        return round(self._precipitationTotal.iloc[offset//24])

    def getMaxTempCelc(self, offset=0):
        return round(self._maxTempCelc.iloc[offset//24])

    def getMinTempCelc(self, offset=0):
        return round(self._minTempCelc.iloc[offset//24])


if __name__ == '__main__':
    testSite = Location(52.52, 13.41, "Toronto")
    print("Location testing:\n")

    print("Max temp today: ", testSite.getMaxTempCelc())
    print("Max temp tomorrow: ", testSite.getMaxTempCelc(offset=24))

    print("Min temp today: ", testSite.getMinTempCelc())
    print("Min temp tomorrow: ", testSite.getMinTempCelc(offset=24))

    print("Precipitation total today: ", testSite.getPrecipitationTotal())
    print("Precipitation total 2 days from now: ", testSite.getPrecipitationTotal(48))

    print("Wind direction current: ", testSite.getWindDirection())
    print("Wind direction 8 hours from now: ", testSite.getWindDirection(offset=8))

    print("UV index current: ", testSite.getUVIndex())
    print("UV index 20 hours from now: ", testSite.getUVIndex(offset=20))

    print("Weather name current: ", testSite.getWeatherName())
    print("Weather name 96 hours from now: ", testSite.getWeatherName(offset=96))

    print("Icon name current: ", testSite.getIconName())
    print("Icon name 96 hours from now: ", testSite.getIconName(offset=96))
