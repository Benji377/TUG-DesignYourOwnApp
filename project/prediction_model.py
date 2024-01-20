import os
import joblib
import pandas as pd


# I created this model myself and published it on Kaggle. It has an accuracy of +/- 0.4 degrees Celsius.
# Kaggle URL: https://www.kaggle.com/code/benben377/weather-forecasting/
# Weather data used for the model goes from 2018-05-01 to 2023-09-01

class WeatherModel:
    """
    A class representing a weather prediction model.

    Attributes:
        WEATHER_MODEL: The loaded weather prediction model.
        WEATHER_DATA: The weather data used for prediction.

    Methods:
        __init__: Initializes the WeatherModel object by loading the model from the assets folder.
        predict: Makes a weather prediction based on the input features.

    """

    WEATHER_MODEL = None
    WEATHER_DATA = None

    def __init__(self):
        """
        Initializes the WeatherModel object by loading the model from the assets folder.
        """
        model_path = os.path.join(os.path.dirname(__file__), 'assets', 'saved_model.pkl')
        with open(model_path, 'rb') as file:
            loaded_model = joblib.load(file)
        self.WEATHER_MODEL = loaded_model

    def predict(self, tempmax, tempmin, uvindex, feelslikemax, feelslikemin):
        """
        Makes a weather prediction based on the input features.

        Parameters:
            tempmax: The maximum temperature.
            tempmin: The minimum temperature.
            uvindex: The UV index.
            feelslikemax: The maximum feels-like temperature.
            feelslikemin: The minimum feels-like temperature.

        Returns:
            The predicted temperature.

        """
        input_features = pd.DataFrame({
            'tempmax': [tempmax],
            'tempmin': [tempmin],
            'uvindex': [uvindex],
            'feelslikemax': [feelslikemax],
            'feelslikemin': [feelslikemin]
        })
        predicted_temperature = self.WEATHER_MODEL.predict(input_features)[0]
        return round(predicted_temperature, 2)
