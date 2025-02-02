import requests
from flask import Flask, render_template,redirect,url_for,flash

app = Flask(__name__)

city_name = 'malappuram'
API_Key =  '8ebe3193fb021551c841b7d96b418a45'
url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'



response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is ', data['weather'][0]['description'])
    print('Current Temperature is ',data['main']['temp'])
    print('Current Temperature feels like ',data['main']['feels_like'])
    print('Current humidity is ',data['main']['humidity'])




# @app.route('/')
# def index():
#     return 'hello world'

# if __name__ == '__main__':
#     app.run(debug=True)