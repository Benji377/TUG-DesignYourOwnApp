import datetime
import os
import tkinter as tk
import ttkbootstrap as ttk
import json
from project.weather_data import WeatherData
from ttkbootstrap.toast import ToastNotification


def save_file(file_name, data):
    """
    Save the data to a JSON file with the given file name.

    Parameters:
        file_name (str): The name of the file to save.
        data (dict): The data to be saved.

    Returns:
        None
    """

    home_directory = os.path.expanduser("~")
    if os.name in {"posix", "nt"}:  # macOS, Linux, and Windows
        download_folder = os.path.join(home_directory, "Downloads")
    else:
        # Handle other operating systems if necessary
        download_folder = home_directory

    file_path = os.path.join(download_folder, file_name)

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

    print(f"File downloaded successfully to: {file_path}")
    ToastNotification(
        title="Weather data downloaded",
        message=f"File downloaded successfully to: {file_path}",
        duration=3000,
        alert=True
    ).show_toast()


class InfoPage(tk.Frame):
    """
    A class representing the information page of the application.

    Parameters:
        parent (tkinter.Tk): The parent widget.
        controller (tkinter.Tk): The controller widget.

    Attributes:
        weather_data (WeatherData): An instance of the WeatherData class.
        nav_bar (ttk.Frame): The navigation bar widget.
        settings_button (ttk.Button): The button to go back to the main page.
        setting_label (ttk.Label): The label for the information page.
        weather_data_button (ttk.Button): The button to download weather data.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.weather_data = WeatherData()

        self.nav_bar = ttk.Frame(self, height=20, width=50)
        self.nav_bar.pack(side=tk.TOP, fill=tk.X)

        from project.pages.main_page import MainPage
        self.settings_button = ttk.Button(self.nav_bar, text="Home",
                                          command=lambda: controller.show_frame(MainPage),
                                          style='primary.TButton')
        self.settings_button.pack(side=tk.RIGHT, padx=10, pady=5)

        self.setting_label = ttk.Label(self.nav_bar, text="Information")
        self.setting_label.pack(side=tk.LEFT, padx=10, pady=5)

        # Labels for headings
        units_heading = tk.Label(self, text="Units", font=("Helvetica", 14, "bold"))
        units_heading.pack(anchor="w", padx=10, pady=5)

        print(self.weather_data.get_units())

        for unit, value in self.weather_data.get_units().items():
            if unit.endswith("_2m"):
                unit = unit[:-3]
            if "_" in unit:
                unit = unit.replace("_", " ")
            if unit == "relativehumidity":
                unit = "Relative humidity"
            unit = unit[0].upper() + unit[1:]
            unit_label = tk.Label(self, text=f"{unit}: {value}")
            unit_label.pack(anchor="w", padx=20, pady=5)

        ml_model_heading = tk.Label(self, text="Machine Learning Model", font=("Helvetica", 14, "bold"))
        ml_model_heading.pack(anchor="w", padx=10, pady=5)

        url_label = tk.Label(self, text="URL: https://www.kaggle.com/datasets/benben377/weather-data-graz")
        url_label.pack(anchor="w", padx=20, pady=5)

        model_type_label = tk.Label(self, text="Type: Machine Learning - Random Forest Regression")
        model_type_label.pack(anchor="w", padx=20, pady=5)

        accuracy_label = tk.Label(self, text="Accuracy: +-0.4°C")
        accuracy_label.pack(anchor="w", padx=20, pady=5)

        # Button for downloading weather data for the next 7 days
        self.weather_data_button = ttk.Button(self, text="Download Weather Data",
                                              command=self.download_weather_data,
                                              style='primary.TButton')
        self.weather_data_button.pack(pady=10)

    def download_weather_data(self):
        """
        Download weather data for the next 7 days and save it to a JSON file.

        Returns:
            None
        """
        weather_data_list = []
        current_date = datetime.datetime.now().date()
        for day_index in range(6):  # Weather data for the next 7 days (excluding today)
            day_weather = self.weather_data.get_daily_weather(day_index)
            forecast_date = current_date + datetime.timedelta(days=day_index)
            daily_data = {
                "day": forecast_date.strftime('%Y-%m-%d'),
                "temperature": day_weather["temperature"],
                "feels_like": self.weather_data.get_daily_feels_temp()[day_index],
                "prediction": self.weather_data.get_daily_predicted_temp()[day_index]
            }
            weather_data_list.append(daily_data)

        save_file("weather_data.json", weather_data_list)
