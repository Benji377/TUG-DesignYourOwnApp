# Some helper functions for weather codes. The API returns codes that need to be interpreted.
# Depending on the code, we return a status, a description and a path to an image.

def weather_description(code):
    """
    Get the weather description based on the given code.

    Parameters:
        code (int): The weather code.

    Returns:
        str: The corresponding weather description. If the code is not found in the weather_codes dictionary,
             "Unknown weather code" is returned.
    """
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog and depositing rime fog",
        48: "Fog and depositing rime fog",
        51: "Drizzle: Light intensity",
        53: "Drizzle: Moderate intensity",
        55: "Drizzle: Dense intensity",
        56: "Freezing Drizzle: Light intensity",
        57: "Freezing Drizzle: Dense intensity",
        61: "Rain: Slight intensity",
        63: "Rain: Moderate intensity",
        65: "Rain: Heavy intensity",
        66: "Freezing Rain: Light intensity",
        67: "Freezing Rain: Heavy intensity",
        71: "Snow fall: Slight intensity",
        73: "Snow fall: Moderate intensity",
        75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight intensity",
        81: "Rain showers: Moderate intensity",
        82: "Rain showers: Violent intensity",
        85: "Snow showers: Slight intensity",
        86: "Snow showers: Heavy intensity",
        95: "Thunderstorm: Slight intensity",
        96: "Thunderstorm with hail: Slight intensity",
        99: "Thunderstorm with hail: Heavy intensity"
    }

    return weather_codes.get(code, "Unknown weather code")


def weather_image_path(code):
    """
    Returns the image file path corresponding to the given weather code.

    Parameters:
        code (int): The weather code.

    Returns:
        str: The image file path.

    If the weather code is not found in the weather_codes dictionary, the function
    returns the file path for the "unknown.png" image.
    """
    weather_codes = {
        0: "sunny.png",  # Clear sky
        1: "cloudy.png",  # Mainly clear
        2: "cloudy.png",  # Partly cloudy
        3: "cloudy.png",  # Overcast
        45: "fog.png",  # Fog and depositing rime fog
        48: "fog.png",  # Fog and depositing rime fog
        51: "rain.png",  # Drizzle: Light intensity
        53: "rain.png",  # Drizzle: Moderate intensity
        55: "rain.png",  # Drizzle: Dense intensity
        56: "snow.png",  # Freezing Drizzle: Light intensity
        57: "snow.png",  # Freezing Drizzle: Dense intensity
        61: "rain.png",  # Rain: Slight intensity
        63: "rain.png",  # Rain: Moderate intensity
        65: "rain.png",  # Rain: Heavy intensity
        66: "snow.png",  # Freezing Rain: Light intensity
        67: "snow.png",  # Freezing Rain: Heavy intensity
        71: "snow.png",  # Snow fall: Slight intensity
        73: "snow.png",  # Snow fall: Moderate intensity
        75: "snow.png",  # Snow fall: Heavy intensity
        77: "snow.png",  # Snow grains
        80: "rain.png",  # Rain showers: Slight intensity
        81: "rain.png",  # Rain showers: Moderate intensity
        82: "rain.png",  # Rain showers: Violent intensity
        85: "snow.png",  # Snow showers: Slight intensity
        86: "snow.png",  # Snow showers: Heavy intensity
        95: "storm.png",  # Thunderstorm: Slight intensity
        96: "storm.png",  # Thunderstorm with hail: Slight intensity
        99: "storm.png"  # Thunderstorm with hail: Heavy intensity
    }

    image_file = weather_codes.get(code, "unknown.png")
    return f"assets/images/{image_file}"


def weather_description_word(code):
    """
    Returns the weather description word based on the given weather code.

    Parameters:
        code (int): The weather code.

    Returns:
        str: The weather description word corresponding to the given code. If the code is not found in the weather_codes dictionary, "Unknown" is returned.
    """

    weather_codes = {
        0: "Sunny",  # Clear sky
        1: "Partly cloudy",  # Mainly clear
        2: "Partly cloudy",  # Partly cloudy
        3: "Cloudy",  # Overcast
        45: "Foggy",  # Fog and depositing rime fog
        48: "Foggy",  # Fog and depositing rime fog
        51: "Drizzle",  # Drizzle: Light intensity
        53: "Drizzle",  # Drizzle: Moderate intensity
        55: "Drizzle",  # Drizzle: Dense intensity
        56: "Freezing drizzle",  # Freezing Drizzle: Light intensity
        57: "Freezing drizzle",  # Freezing Drizzle: Dense intensity
        61: "Rain",  # Rain: Slight intensity
        63: "Rain",  # Rain: Moderate intensity
        65: "Rain",  # Rain: Heavy intensity
        66: "Freezing rain",  # Freezing Rain: Light intensity
        67: "Freezing rain",  # Freezing Rain: Heavy intensity
        71: "Snow",  # Snow fall: Slight intensity
        73: "Snow",  # Snow fall: Moderate intensity
        75: "Snow",  # Snow fall: Heavy intensity
        77: "Snow",  # Snow grains
        80: "Rain showers",  # Rain showers: Slight intensity
        81: "Rain showers",  # Rain showers: Moderate intensity
        82: "Rain showers",  # Rain showers: Violent intensity
        85: "Snow showers",  # Snow showers: Slight intensity
        86: "Snow showers",  # Snow showers: Heavy intensity
        95: "Thunderstorm",  # Thunderstorm: Slight intensity
        96: "Thunderstorm with hail",  # Thunderstorm with hail: Slight intensity
        99: "Thunderstorm with hail"  # Thunderstorm with hail: Heavy intensity
    }

    return weather_codes.get(code, "Unknown")
