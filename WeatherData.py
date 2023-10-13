from tkinter import *
from ParseJson import *
from WeatherApp import get_weather_data
from PIL import ImageTk, Image
import requests

from Constants import LOCATION_HEIGHT, CURRENT_DAY_HEIGHT, NEXT_DAY_HEIGHT, TEXT_BOX_WIDTH

# There is some fairly repeated code in this file, but breaking it into functions would require some
# extra parameters that at this moment would rather lessen readability
def display_data(location, result_frame, days=0):
    # have to clear the previous display
    for widget in result_frame.winfo_children():
        widget.destroy()

    # deal with invalid location names
    try:
        weather_info = get_weather_data(location, days)
    except RuntimeError:
        error = Text(result_frame, width=TEXT_BOX_WIDTH, height=2)
        error.insert(INSERT, "Location not found! Please try again.")
        error.grid(row=0)
        return

    # get the weather information. today is always shown
    location_data = create_location(weather_info["location"])
    current_data = create_current_weather(weather_info["current"])
    today_forecast = create_forecast_day(weather_info["forecast"]["forecastday"], 0)

    # output the location and today's weather
    entry = Text(result_frame, pady=10, height=LOCATION_HEIGHT, width=TEXT_BOX_WIDTH)
    entry.insert("1.0", write_location(location_data))
    entry.grid(row=0, column=0, sticky=W)

    entry = Text(result_frame, pady=10, height=CURRENT_DAY_HEIGHT, width=TEXT_BOX_WIDTH)
    entry.insert("1.0", write_current_weather(current_data, today_forecast))
    entry.grid(row=1, column=0)

    icon = ImageTk.PhotoImage(Image.open(requests.get("https:" + current_data['icon'], stream=True).raw))
    entry = Label(result_frame, image=icon, width=icon.width(), height=icon.height())
    entry.image = icon
    entry.grid(row=1, column=1, sticky=N + W)

    # dealing with following requested days
    for day_index in range(1, days):
        next_day_forecast = create_forecast_day(weather_info["forecast"]["forecastday"], day_index)
        entry = Text(result_frame, pady=10, height=NEXT_DAY_HEIGHT, width=TEXT_BOX_WIDTH)
        entry.insert("1.0", write_forecast(next_day_forecast))
        entry.grid(row=1 + day_index, column=0)

        icon = ImageTk.PhotoImage(Image.open(requests.get("https:" + next_day_forecast['icon'], stream=True).raw))
        entry = Label(result_frame, image=icon, width=icon.width(), height=icon.height())
        entry.image = icon
        entry.grid(row=1 + day_index, column=1, sticky=N + W)

