import requests

import Constants


def get_weather_data(location, days=0):
    params = {
        "key": Constants.API_KEY,
        "q": location,
        "days": days
    }

    # for this implementation, we make the same request to the API, so it's a constant
    # however, for a more complex program that uses more of the API functionality, it could be a parameter
    response = requests.get(Constants.API_URL + Constants.API_REQUEST, params)

    if response.status_code == 200:
        weather_info = response.json()
        return weather_info

    else:
        raise RuntimeError("City not found!")

