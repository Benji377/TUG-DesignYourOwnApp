import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.style as style
from PIL import Image, ImageTk
import datetime
from project.weather_codes import weather_image_path, weather_description
from project.weather_data import WeatherData
import os

def get_current_week_day():
    """
    Get the current day of the week.

    Returns:
        list: A list of the current day of the week and the next 6 days.
    """
    current_day_index = datetime.datetime.now().weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return [days_of_week[(current_day_index + i) % 7] for i in range(7)]


class MainPage(tk.Frame):
    """
    The main page of the application.

    Parameters:
        parent (tkinter.Tk): The parent widget.
        controller (tkinter.Tk): The controller widget.

    Attributes:
        days_of_week (list): A list of the current day of the week and the next 6 days.
        weather_data (WeatherData): An instance of the WeatherData class.
        current_weather_data (dict): The current weather data.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.days_of_week = get_current_week_day()

        self.weather_data = WeatherData()
        self.current_weather_data = self.weather_data.get_current_weather()

        self.setup_ui(controller)
        self.update_info(xdata=0)
        self.update_time()

    def setup_ui(self, controller):
        """
        Set up the user interface.

        Parameters:
            controller (tkinter.Tk): The controller widget.
        """
        self.setup_left_frame()
        self.setup_navigation_bar(controller)
        self.setup_weather_plot()

    def setup_left_frame(self):
        """
        Set up the left frame of the user interface.
        """
        self.left_frame = ttk.Frame(self, width=200, padding=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        weather_code_img = (Image.open(os.path.join(dir_path, weather_image_path(
            self.weather_data.get_current_weather()['weathercode']))).resize((50, 50), Image.LANCZOS))
        self.weather_code_img_tk = ImageTk.PhotoImage(weather_code_img)
        self.weathercode_label = ttk.Label(self.left_frame, image=self.weather_code_img_tk)
        self.weathercode_label.pack()

        self.weather_desc_label = ttk.Label(self.left_frame, text='N/A')
        self.weather_desc_label.pack()

        icon_paths = ["assets/icons/thermometer.png", "assets/icons/humidity.png", "assets/icons/barometer.png",
                      "assets/icons/wind.png", "assets/icons/visibility.png", "assets/icons/sunrise.png",
                      "assets/icons/sunset.png", "assets/icons/prediction.png", "assets/icons/feelslike.png"]

        self.icons = [Image.open(os.path.join(dir_path, path)).resize((30, 30), Image.LANCZOS) for path in icon_paths]
        self.icon_images = [ImageTk.PhotoImage(image) for image in self.icons]

        labels_text = ["Temperature: N/A°C", "Humidity: N/A", "Pressure: N/A", "Windspeed: N/A",
                       "Visibility: N/A", "Sunrise: N/A", "Sunset: N/A", "Prediction: N/A", "Feels: N/A"]

        self.labels = {}
        for i, text in enumerate(labels_text):
            label = ttk.Label(self.left_frame, text=text, image=self.icon_images[i], compound=tk.LEFT, anchor=tk.W)
            label.pack(fill=tk.X, padx=5, pady=15)
            self.labels[text.split(":")[0].strip().lower()] = label

    def setup_navigation_bar(self, controller):
        """
        Set up the navigation bar of the user interface.

        Parameters:
            controller (tkinter.Tk): The controller widget.
        """
        self.nav_bar = ttk.Frame(self, height=20, width=50)
        self.nav_bar.pack(side=tk.TOP, fill=tk.X)

        from project.pages.info_page import InfoPage
        self.settings_button = ttk.Button(self.nav_bar, text="Info",
                                          command=lambda: controller.show_frame(InfoPage),
                                          style='primary.TButton')
        self.settings_button.pack(side=tk.RIGHT, padx=10, pady=5)

        self.time_label = ttk.Label(self.nav_bar, text="N/A")
        self.time_label.pack(side=tk.RIGHT, padx=10, pady=5)

    def setup_weather_plot(self):
        """
        Set up the weather plot.
        """
        style.use('dark_background')
        self.daily_temp = self.weather_data.get_daily_temperature()
        self.daily_feels = self.weather_data.get_daily_feels_temp()
        self.daily_predict = self.weather_data.get_daily_predicted_temp()

        self.fig, self.ax = plt.subplots(figsize=(7, 4))
        self.set_plot_data_endpoints()
        self.set_fixed_plot_data()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas.mpl_connect('button_press_event', self.update_info)

    def update_info(self, event=None, xdata=None):
        """
        Update the weather information based on the selected day.

        Parameters:
            event (tkinter.Event): The event object.
            xdata (float): The x-coordinate of the selected point on the plot.
        """
        if event is not None and event.xdata is not None:
            day_index = round(event.xdata)
        elif xdata is not None:
            day_index = round(xdata)
        else:
            day_index = 0

        self.ax.clear()
        self.set_plot_data_endpoints()
        self.ax.plot(self.days_of_week[day_index], self.daily_temp[day_index], marker='o', color='y')
        self.set_fixed_plot_data()
        # Redraw the canvas
        self.canvas.draw()

        if day_index == 0:
            self.set_today_weather_data()
        else:
            self.set_day_weather_data(day_index)

    def set_today_weather_data(self):
        """
        Set the weather data for the current day.
        """
        current_weather = self.weather_data.get_current_weather()
        self.weather_desc_label.config(text=weather_description(current_weather['weathercode']))
        self.update_label("temperature", f'Temperature: {current_weather["temperature"]}')
        self.update_label("humidity", f"Humidity: {current_weather['humidity']}")
        self.update_label("pressure", f"Pressure: {current_weather['pressure']}")
        self.update_label("windspeed", f"Windspeed: {current_weather['windspeed']}")
        self.update_label("visibility", f"Visibility: {current_weather['visibility']}")
        self.update_label("sunrise", f"Sunrise: {current_weather['sunrise']}")
        self.update_label("sunset", f"Sunset: {current_weather['sunset']}")
        self.update_label("prediction", 'N/A', "hidden")
        self.update_label("feels", 'N/A', "hidden")

    def set_day_weather_data(self, day_index):
        """
        Set the weather data for the selected day.

        Parameters:
            day_index (int): The index of the selected day.
        """
        day_weather = self.weather_data.get_daily_weather(day_index)
        self.weather_desc_label.config(text=weather_description(day_weather['weathercode']))
        self.update_label("temperature", f'Temperature: {day_weather["temperature"]} °C')
        self.update_label("prediction", f'Prediction: {self.daily_predict[day_index]} °C')
        self.update_label("feels", f'Feels like: {self.daily_feels[day_index]} °C')

        print(day_weather)
        weather_code_img = (Image.open(weather_image_path(day_weather['weathercode']))
                            .resize((50, 50), Image.LANCZOS))
        self.weather_code_img_tk = ImageTk.PhotoImage(weather_code_img)
        self.weathercode_label.config(image=self.weather_code_img_tk)
        self.update_label("humidity", "", "hidden")
        self.update_label("pressure", "", "hidden")
        self.update_label("windspeed", "", "hidden")
        self.update_label("visibility", "", "hidden")
        self.update_label("sunrise", "", "hidden")
        self.update_label("sunset", "", "hidden")

    def set_fixed_plot_data(self):
        """
        Set the fixed data for the weather plot.
        """
        self.ax.set_ylabel('Temperature (°C)')
        self.ax.set_xlabel('Day')
        self.ax.set_title('Weekly Weather Forecast')
        self.ax.legend()

    def set_plot_data_endpoints(self):
        """
        Set the data endpoints for the weather plot.
        """
        self.ax.plot(
            self.days_of_week,
            self.daily_temp,
            marker='o',
            color='b',
            label="Temperature",
        )
        self.ax.plot(
            self.days_of_week,
            self.daily_feels,
            marker='o',
            color='r',
            label="Feels like",
        )
        self.ax.plot(
            self.days_of_week,
            self.daily_predict,
            marker='o',
            color='g',
            label="Predicted Temperature",
        )

    def update_label(self, label_key, new_text, state="normal"):
        """
        Update the text and state of a label.

        Parameters:
            label_key (str): The key of the label.
            new_text (str): The new text for the label.
            state (str): The state of the label. Default is "normal".
        """
        if label := self.labels.get(label_key.lower()):
            if state == "hidden":
                label.pack_forget()
            else:
                label.config(text=new_text, state=state)
                label.pack(fill=tk.X, padx=5, pady=15)

    def update_time(self):
        """
        Update the current time label.
        """
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time_label.config(text=f"Current Time: {current_time}")
        self.after(1000, self.update_time)
