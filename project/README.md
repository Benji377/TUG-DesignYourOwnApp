# Main Project: GrazWeatherML

## Project Overview
GrazWeatherML is a specialized weather prediction tool designed for the city of Graz, Austria. It leverages a bespoke Machine Learning model, meticulously trained on localized weather data from Graz, to provide accurate forecasts. The tool integrates seamlessly with the OpenWeatherMap API, retrieving real-time weather information and employing the ML model to predict weather conditions for the next 7 days.

### Highlights:
- **Custom Machine Learning Model:** Crafted to forecast Graz's weather patterns, this model forms the backbone of the project.
- **Interactive UI with ttk Bootstrap:** The user interface, built on ttk bootstrap (an enhanced version of tkinter), ensures an aesthetically pleasing and user-friendly experience.
- **Temperature Discrepancy Visualization:** The primary goal is to present users with a side-by-side comparison of the ML-predicted temperature and the actual temperature.

### Key Features:
- **In-House Machine Learning Model:** Developed to enhance precision in weather predictions for Graz.
- **Comprehensive Documentation:** The project features pdoc3-generated HTML documentation, accessible in the "docs" folder.
- **Backend Testing with Pytest:** The project's backend is rigorously tested using the Pytest framework.

### Project Components:
- **`main.py`:** The central file orchestrating the execution of the entire project.
- **Weather API Integration:** Connects to the OpenWeatherMap API to fetch current temperature and relevant weather factors.
- **Machine Learning Model:** Engineered to forecast weather conditions based on Graz-specific data.
- **Two-Page UI:**
  - *Main Page:* Offers users a snapshot of current weather conditions and the ML-predicted weather for the upcoming 7 days.
  - *Info Page:* Provides users with insights into the units employed in the project and details about data sources.

## Dependencies

List external dependencies you used in this project and the reason for their inclusion in the following table:

|   Dependency   | Reason for inclusion                                                                                          |
|:--------------:|:--------------------------------------------------------------------------------------------------------------|
|    `pytest`    | Testing implementations in this project using automatic test cases.                                           |
|    `httpx`     | The faster alternative to requests. Used to make calls to the weather API                                     |
|    `pandas`    | A framework to structure data. Used to feed the ML model with parameters                                      |
|    `joblib`    | Loads pretrained ML models and makes them usable in external code                                             |
| `scikit-learn` | Is needed because the machine learning model was trained on this. Without it, the ML model would fail loading |
| `ttkbootstrap` | Adds a bootstrap style layer to the default tkinter to make it more visually appealing                        |
|    `pdoc3`     | Generates an HTML documentation of the project (not needed to run the app)                                    |
