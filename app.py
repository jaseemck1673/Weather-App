import requests
from api import API_Key
from flask import Flask, render_template,redirect,url_for,flash

app = Flask(__name__)

city_name = 'New Delhi'
# url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'
url = f'api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_Key}'
@app.route('/')
def index():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        print('Weather is ', data['weather'][0]['description'])
        print('Current Temperature is ',data['main']['temp'])
        print('Current Temperature feels like ',data['main']['feels_like'])
        print('Current humidity is ',data['main']['humidity'])
        print('Current humidity is ',data['name'])
        return render_template('index.html',datas=data)

if __name__ == '__main__':
    app.run(debug=True)
 
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print('Weather is ', data['weather'][0]['description'])
#     print('Current Temperature is ',data['main']['temp'])
#     print('Current Temperature feels like ',data['main']['feels_like'])
#     print('Current humidity is ',data['main']['humidity'])




