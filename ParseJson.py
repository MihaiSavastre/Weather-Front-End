# this processing perhaps could have been done with the json package or something else
# but I have not found the way to do so
# at the bottom there are some functions that transform dictionaries containing the weather info
# into strings

# moreover, there might be a more elegant solution in writing all this information
# as fields of a class, but this will do
import datetime

# this could be passed as a parameter to have customizable date formats
date_format = "%d-%m-%Y"


def create_location(weatherAPI_location):
    location = {}
    location.update({"name": weatherAPI_location["name"]})
    location.update({"region": weatherAPI_location["region"]})
    location.update({"country": weatherAPI_location["country"]})
    location.update({"localtime": weatherAPI_location["localtime"]})
    return location


def create_current_weather(weatherAPI_current, unit='c'):
    current = {}
    current.update({"temp": weatherAPI_current["temp_" + unit]})
    current.update({"humidity": weatherAPI_current["humidity"]})
    current.update({"cloud": weatherAPI_current["cloud"]})
    current.update({"uv": weatherAPI_current["uv"]})
    current.update({"icon": weatherAPI_current["condition"]["icon"]})
    return current


def create_forecast_day(weatherAPI_forecastday, day_index, unit='c'):
    forecast = {}
    weatherAPI_forecastday_date = weatherAPI_forecastday[day_index]

    # API gives the date as a string Y-m-d, so we need to transform it in datetime
    date_comps = map(int, weatherAPI_forecastday_date["date"].split("-"))
    date = datetime.date(*date_comps)
    forecast.update({"date": date})
    forecast.update({"maxtemp": weatherAPI_forecastday_date["day"]["maxtemp_" + unit]})
    forecast.update({"mintemp": weatherAPI_forecastday_date["day"]["mintemp_" + unit]})
    forecast.update({"avgtemp": weatherAPI_forecastday_date["day"]["avgtemp_" + unit]})
    forecast.update({"daily_chance_of_rain": weatherAPI_forecastday_date["day"]["daily_chance_of_rain"]})
    forecast.update({"daily_chance_of_snow": weatherAPI_forecastday_date["day"]["daily_chance_of_snow"]})
    forecast.update({"icon": weatherAPI_forecastday_date["day"]["condition"]["icon"]})
    return forecast


def write_location(location):
    return f"Location: {location['name']}\n" \
           f"Region: {location['region']}\n" \
           f"Country: {location['country']}\n" \
           f"LocalTime: {location['localtime']}"


def write_current_weather(current, forecast):
    return f"The weather for today is:\n" \
           f"Temperature: {current['temp']}\n" \
           f"High: {forecast['maxtemp']}\n" \
           f"Low: {forecast['mintemp']}\n" \
           f"Average: {forecast['avgtemp']}\n" \
           f"Humidity: {current['humidity']}\n" \
           f"Cloud Level: {current['cloud']}\n" \
           f"UV Index: {current['uv']}\n" \
           f"Chance of rain: {forecast['daily_chance_of_rain']}\n" \
           f"Chance of snow: {forecast['daily_chance_of_snow']}\n"


def write_forecast(forecast):
    return f"The weather for {forecast['date'].strftime(date_format)} is:\n" \
           f"High: {forecast['maxtemp']}\n" \
           f"Low: {forecast['mintemp']}\n" \
           f"Average: {forecast['avgtemp']}\n" \
           f"Chance of rain: {forecast['daily_chance_of_rain']}\n" \
           f"Chance of snow: {forecast['daily_chance_of_snow']}\n"
