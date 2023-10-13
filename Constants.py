API_URL = "http://api.weatherapi.com/v1"
API_KEY = "7430528037664a3d8df213403230310"
API_REQUEST = "/forecast.json"

# Some magic numbers to make Tkinter play nice
# For displaying forecasts
LOCATION_HEIGHT = 5
CURRENT_DAY_HEIGHT = 11
NEXT_DAY_HEIGHT = 7
TEXT_BOX_WIDTH = 50

# For adjusting the frame size in relation to text box size (too small a value for this field will
# make the weather icons not show)
FORECAST_DISPLAY_WIDTH = TEXT_BOX_WIDTH * 9.4
