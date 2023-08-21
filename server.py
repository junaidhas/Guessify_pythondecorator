from flask import Flask,render_template
import requests
import datetime
app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year = current_year)

@app.route("/<username>")
def guess(username):
    AGIFY_data = requests.get(f"https://api.agify.io?name={username}").json()
    user_age = AGIFY_data["age"]
    Gender_data = requests.get(f"https://api.genderize.io?name={username}").json()
    user_gender = Gender_data["gender"]
    Nationality_data = requests.get(f"https://api.nationalize.io?name={username}").json()
    user_country = Nationality_data["country"][0]["country_id"]
    return render_template("guess.html",name = username,age=user_age,gender=user_gender, country=user_country)


if __name__=="__main__":
    app.run(debug=True)
