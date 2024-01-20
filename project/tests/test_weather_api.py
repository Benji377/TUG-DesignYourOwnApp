import pytest
from unittest.mock import patch, Mock
from project.weather_data import WeatherData


@pytest.fixture
def mock_weather_data():
    return {
        "current": {
            "temperature_2m": 20,
            "relativehumidity_2m": 50,
            "apparent_temperature": 19,
            "weathercode": 1,
            "surface_pressure": 1000,
            "windspeed_10m": 5
        },
        "current_units": {
            "temperature_2m": "C",
            "relativehumidity_2m": "%",
            "apparent_temperature": "C",
            "weathercode": "code",
            "surface_pressure": "hPa",
            "windspeed_10m": "km/h"
        },
        "hourly": {
            "time": ["2022-04-01T00:00:00"],
            "visibility": [10000]
        },
        "hourly_units": {
            "visibility": "m"
        },
        "daily": {
            "time": ["2022-04-01"],
            "sunrise": ["2022-04-01T06:00:00"],
            "sunset": ["2022-04-01T20:00:00"],
            "temperature_2m_max": [25, 25, 25, 25, 25, 25, 25],
            "temperature_2m_min": [15, 15, 15, 15, 15, 15, 15],
            "apparent_temperature_max": [24, 24, 24, 24, 24, 24, 24],
            "apparent_temperature_min": [16, 16, 16, 16, 16, 16, 16],
            "uv_index_max": [5, 5, 5, 5, 5, 5, 5],
            "weathercode": [1, 1, 1, 1, 1, 1, 1]
        }
    }


@pytest.fixture
def mock_response(mock_weather_data):
    response = Mock()
    response.status_code = 200
    response.json.return_value = mock_weather_data
    return response


@pytest.fixture
def mock_httpx_get(mock_response):
    with patch('httpx.get', return_value=mock_response) as mock:
        yield mock


@pytest.fixture
def weather_data(mock_httpx_get):
    return WeatherData()


def test_init(weather_data, mock_httpx_get):
    # Assert
    mock_httpx_get.assert_called_once_with(WeatherData.API_URL)
    assert weather_data.WEATHER_JSON is not None


def test_get_units(weather_data):
    # Act
    units = weather_data.get_units()

    # Assert
    assert units == {
        "temperature_2m": "C",
        "relativehumidity_2m": "%",
        "apparent_temperature": "C",
        "weathercode": "code",
        "surface_pressure": "hPa",
        "windspeed_10m": "km/h",
        "visibility": "m"
    }


def test_find_closest_time_index(weather_data):
    # Act
    index = weather_data.find_closest_time_index()

    # Assert
    assert index == 0


def test_get_current_visibility(weather_data):
    # Act
    visibility = weather_data.get_current_visibility()

    # Assert
    assert visibility == 10


def test_get_predicted_temp(weather_data):
    # Arrange
    weather_data.forecast_model.predict = Mock(return_value=20)

    # Act
    predicted_temp = weather_data.get_predicted_temp()

    # Assert
    weather_data.forecast_model.predict.assert_called_once_with(25, 15, 5, 24, 16)
    assert predicted_temp == 20


def test_get_current_weather(weather_data):
    # Arrange
    weather_data.get_predicted_temp = Mock(return_value=20)

    # Act
    current_weather = weather_data.get_current_weather()

    # Assert
    assert current_weather == {
        "temperature": "20 C",
        "predicted_temp": 20,
        "humidity": "50 %",
        "feels_like": "19 C",
        "weathercode": 1,
        "pressure": "1000 hPa",
        "windspeed": "5 km/h",
        "visibility": "10.0 km",
        "sunrise": "06:00",
        "sunset": "20:00"
    }


def test_get_daily_weather(weather_data):
    # Arrange
    weather_data.forecast_model.predict = Mock(return_value=20)

    # Act
    daily_weather = weather_data.get_daily_weather(0)

    # Assert
    assert daily_weather == {
        "day_name": "Friday",
        "weathercode": 1,
        "temperature": "20.0",
        "predicted_temp": 20,
        "feels_like": "20.0"
    }


def test_get_daily_temperature(weather_data):
    # Act
    daily_temperature = weather_data.get_daily_temperature()

    # Assert
    assert daily_temperature == [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]


def test_get_daily_feels_temp(weather_data):
    # Act
    daily_feels_temp = weather_data.get_daily_feels_temp()

    # Assert
    assert daily_feels_temp == [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]


def test_get_daily_predicted_temp(weather_data):
    # Arrange
    weather_data.forecast_model.predict = Mock(return_value=20)

    # Act
    daily_predicted_temp = weather_data.get_daily_predicted_temp()

    # Assert
    assert daily_predicted_temp == [20, 20, 20, 20, 20, 20, 20]
