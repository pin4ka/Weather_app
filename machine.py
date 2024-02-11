# import modules
import datetime, requests

""" 
Onno API add korar jonno sei api er notun function define korbo
"api_key" folder e API key rakbo
api choice condition e notun option add korbo 
"""


# api choice condition
def weather_data(api_name, city):
    if api_name == "1":
        print("<<<<<<<<<<<<<<<<<<<<| open weather api |>>>>>>>>>>>>>>>>>>>>\n")
        return weather_data_open_weather(city)
    elif api_name == "2":
        print("<<<<<<<<<<<<<<<<<<<<| api ninjas api |>>>>>>>>>>>>>>>>>>>>\n")
        return weather_data_api_ninja(city)
    else:
        print("<<<<<<<<<<<<<<<<<<<<| api ninjas api by default |>>>>>>>>>>>>>>>>>>>>\n")
        return weather_data_api_ninja(city)


# open weather API
def weather_data_open_weather(city):
    # open api key || save api key as "output.rax" in main directory
    with open("./api_key/openweather", "r") as file_file:
        api_key = file_file.read()
    api_url = "http://api.openweathermap.org/data/2.5/weather?appid="
    url = f"{api_url}{api_key}&q={city}"
    api_request = requests.get(url).json()
    # city = input_url[1]
    try:
        if api_request["cod"] == "404":
            print(api_request["message"])
            return [api_request["message"]]

        elif api_request["cod"] != "404":
            usr_current_time = (datetime.datetime.now()).strftime("%H:%M:%S")
            usr_current_date = (datetime.datetime.now()).strftime("%d-%m-%Y")
            usr_temperature_in_celsius = round(
                ((api_request["main"]["temp"]) - 273.15), 2
            )
            usr_humidity = api_request["main"]["humidity"]
            usr_wind = round((api_request["wind"]["speed"]) * 3.6, 3)
            print(
                f"Weather {city.capitalize()}\t\t\t{usr_current_date}  {usr_current_time}"
            )
            print(f"Temperature is {usr_temperature_in_celsius} deg C")
            print(f"Humidity {usr_humidity} % ")
            print(f"Wind Speed {usr_wind} km/h")
            return [
                city,
                usr_temperature_in_celsius,
                usr_humidity,
                usr_current_time,
                usr_current_date,
                usr_wind,
            ]

        else:
            print("Error...")
            return ["Error"]

    except:
        print("faild to fetch weather data...")
        return ["faild to fetch weather data..."]


# api Ninja weather API
def weather_data_api_ninja(city):
    with open("./api_key/apininja", "r") as file_file:
        api_key = file_file.read()

    api_url = f"https://api.api-ninjas.com/v1/weather?city={city}"
    headers = {"X-Api-Key": api_key}
    response = requests.get(api_url, headers)
    api_request = response.json()
    try:
        if response.status_code == requests.codes.ok:
            usr_current_time = (datetime.datetime.now()).strftime("%H:%M:%S")
            usr_current_date = (datetime.datetime.now()).strftime("%d-%m-%Y")
            usr_temperature_in_celsius = api_request["feels_like"]
            usr_humidity = api_request["humidity"]
            usr_wind = round(api_request["wind_speed"] * 3.6, 3)

            print(
                f"Weather {city.capitalize()}\t\t\t{usr_current_date}  {usr_current_time}"
            )
            print(f"Temperature is {usr_temperature_in_celsius} deg C")
            print(f"Humidity {usr_humidity} % ")
            print(f"Wind Speed {usr_wind} km/h")

            return [
                city,
                usr_temperature_in_celsius,
                usr_humidity,
                usr_current_time,
                usr_current_date,
                usr_wind,
            ]

        else:
            print("Error:", response.status_code, response.text)
            print("Error...")
            return ["Error"]
    except:
        print("faild to fetch weather data...")
        return ["faild to fetch weather data..."]
