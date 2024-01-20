import pytest
from project.prediction_model import WeatherModel


@pytest.fixture
def weather_model_instance():
    # Create an instance of WeatherModel for testing
    return WeatherModel()


def test_weather_model_prediction(weather_model_instance):
    # Test prediction for specific input values
    tempmax = 25
    tempmin = 15
    uvindex = 5
    feelslikemax = 26
    feelslikemin = 16

    # Perform prediction
    predicted_temperature = weather_model_instance.predict(tempmax, tempmin, uvindex, feelslikemax, feelslikemin)

    assert isinstance(predicted_temperature, float)
