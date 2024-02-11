# import modules
from machine import weather_data
from flask import Flask, render_template, request

api_name = "2"  # input("Choose your api[1 for openweather| 2 for apininjas]: ")


# flask app build
weather_app = Flask(__name__)


@weather_app.route("/")
def home():
    return render_template("index.html")


@weather_app.route("/", methods=["POST"])
def weather():
    try:
        user_entered_location = request.form["location_select"]
        # data = weather_data_open_weather(user_entered_location)
        data = weather_data(api_name, user_entered_location)
        print("\nSecessful quary ..... \n")
        return render_template(
            "index.html",
            location=data[0],
            temperat=int(data[1]),
            humidity=data[2],
            time=data[3],
            date=data[4],
            wind_speed=data[5],
        )
    except:
        print("\n\nSomething wrong.........!!!!!!!!!!\n")
        return home()


weather_app.run(debug=True, port=8290)
