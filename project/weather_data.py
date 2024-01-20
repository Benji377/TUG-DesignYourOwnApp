import sys
from datetime import datetime
import httpx
from project.prediction_model import WeatherModel


class WeatherData:
    """
    This class is used to get weather data from an API and parse it into a JSON format.
    It provides methods to retrieve various weather information such as current weather, predicted temperature,
    daily weather, and more.
    """

    API_URL = ('https://api.open-meteo.com/v1/forecast?latitude=47.0667&longitude=15.45&current=temperature_2m,'
               'relativehumidity_2m,apparent_temperature,weathercode,surface_pressure,'
               'windspeed_10m&hourly=visibility&daily=weathercode,temperature_2m_max,temperature_2m_min,'
               'apparent_temperature_max,apparent_temperature_min,sunrise,sunset,uv_index_max&timezone=Europe%2FBerlin')
    WEATHER_JSON = None

    def __init__(self):
        """
        Initializes the WeatherData object by fetching weather data from the API and storing it as JSON.
        If the API request fails, the program exits with an error message.
        """
        weather_data = httpx.get(self.API_URL)
        self.forecast_model = WeatherModel()

        if weather_data.status_code == 200:
            self.WEATHER_JSON = weather_data.json()
        else:
            sys.exit("Error: Could not get weather data from API")

    def get_units(self):
        """
        Retrieves the units of measurement for the weather data from the API.

        Returns:
            dict: A dictionary containing the units of measurement.
        """
        units = self.WEATHER_JSON['current_units']
        visibility = self.WEATHER_JSON['hourly_units']['visibility']
        units['visibility'] = visibility
        return units

    def find_closest_time_index(self):
        """
        Finds the index of the closest time in the API data to the current time.

        Returns:
            int: The index of the closest time.
        """
        current_datetime = datetime.now()
        json_dates = [datetime.fromisoformat(date) for date in self.WEATHER_JSON['hourly']['time']]
        time_diffs = [abs(date - current_datetime) for date in json_dates]

        return time_diffs.index(min(time_diffs))

    def get_current_visibility(self):
        """
        Retrieves the current visibility from the API data.

        Returns:
            float: The current visibility in kilometers.
        """
        return self.WEATHER_JSON['hourly']['visibility'][self.find_closest_time_index()] / 1000

    def get_predicted_temp(self):
        """
        Predicts the temperature for the current day using a machine learning model.

        Returns:
            float: The predicted temperature.
        """
        max_temp = self.WEATHER_JSON['daily']['temperature_2m_max'][0]
        min_temp = self.WEATHER_JSON['daily']['temperature_2m_min'][0]

        apparent_max_temp = self.WEATHER_JSON['daily']['apparent_temperature_max'][0]
        apparent_min_temp = self.WEATHER_JSON['daily']['apparent_temperature_min'][0]

        uv_index = self.WEATHER_JSON['daily']['uv_index_max'][0]

        return self.forecast_model.predict(
            max_temp, min_temp, uv_index, apparent_max_temp, apparent_min_temp
        )

    def get_current_weather(self):
        """
        Retrieves the current weather data.

        Returns:
            dict: A dictionary containing the current weather information.
        """
        current_weather = self.WEATHER_JSON['current']
        weather_units = self.get_units()

        sunrise_time = datetime.fromisoformat(self.WEATHER_JSON['daily']['sunrise'][0]).strftime('%H:%M')
        sunset_time = datetime.fromisoformat(self.WEATHER_JSON['daily']['sunset'][0]).strftime('%H:%M')

        return {
            "temperature": str(round(current_weather["temperature_2m"], 1))
                           + ' '
                           + weather_units["temperature_2m"],
            "predicted_temp": self.get_predicted_temp(),
            "humidity": str(current_weather["relativehumidity_2m"])
                        + ' '
                        + weather_units["relativehumidity_2m"],
            "feels_like": str(round(current_weather["apparent_temperature"], 1))
                          + ' '
                          + weather_units["apparent_temperature"],
            "weathercode": current_weather["weathercode"],
            "pressure": str(current_weather["surface_pressure"])
                        + ' '
                        + weather_units["surface_pressure"],
            "windspeed": str(current_weather["windspeed_10m"])
                         + ' '
                         + weather_units["windspeed_10m"],
            "visibility": f'{str(self.get_current_visibility())} k'
                          + weather_units["visibility"],
            "sunrise": sunrise_time,
            "sunset": sunset_time,
        }

    def get_daily_weather(self, day):
        """
        Retrieves the weather data for a specific day.

        Parameters:
            day (int): The index of the day.

        Returns:
            dict: A dictionary containing the weather information for the specified day.
        """
        day_weather = self.WEATHER_JSON['daily']
        avg_temp = (day_weather["temperature_2m_min"][day] + day_weather["temperature_2m_max"][day]) / 2
        avg_feels = (day_weather["apparent_temperature_min"][day] + day_weather["apparent_temperature_max"][day]) / 2

        predicted_temp = self.forecast_model.predict(
            day_weather["temperature_2m_max"][day],
            day_weather["temperature_2m_min"][day],
            day_weather["uv_index_max"][day],
            day_weather["apparent_temperature_max"][day],
            day_weather["apparent_temperature_min"][day]
        )
        return {
            "day_name": datetime.strptime(
                day_weather["time"][day], "%Y-%m-%d"
            ).strftime("%A"),
            "weathercode": day_weather["weathercode"][day],
            "temperature": str(round(avg_temp, 2)),
            "predicted_temp": predicted_temp,
            "feels_like": str(round(avg_feels, 2)),
        }

    def get_daily_temperature(self):
        """
        Retrieves the average temperature for the next 7 days.

        Returns:
            list: A list of average temperatures for each day.
        """
        return self.format_temp_average(
            "temperature_2m_min", "temperature_2m_max"
        )

    def get_daily_feels_temp(self):
        """
        Retrieves the average feels like temperature for the next 7 days.

        Returns:
            list: A list of average feels like temperatures for each day.
        """
        return self.format_temp_average(
            "apparent_temperature_min", "apparent_temperature_max"
        )

    def format_temp_average(self, arg0, arg1):
        """
        Formats the average temperature for a given range of days.

        Parameters:
            arg0 (str): The first parameter for calculating the average temperature.
            arg1 (str): The second parameter for calculating the average temperature.

        Returns:
            list: A list of average temperatures for each day.
        """
        day_weather = self.WEATHER_JSON['daily']
        weekly_temperatures = []
        for day in range(7):
            avg_temp = (day_weather[arg0][day] + day_weather[arg1][day]) / 2
            weekly_temperatures.append(round(avg_temp, 2))
        return weekly_temperatures

    def get_daily_predicted_temp(self):
        """
        Retrieves the predicted temperature for the next 7 days.

        Returns:
            list: A list of predicted temperatures for each day.
        """
        day_weather = self.WEATHER_JSON['daily']
        weekly_temperatures = []

        for day in range(7):
            predicted_temp = self.forecast_model.predict(
                day_weather["temperature_2m_max"][day],
                day_weather["temperature_2m_min"][day],
                day_weather["uv_index_max"][day],
                day_weather["apparent_temperature_max"][day],
                day_weather["apparent_temperature_min"][day]
            )
            weekly_temperatures.append(predicted_temp)
        return weekly_temperatures
