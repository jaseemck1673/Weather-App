from datetime import datetime
import requests
from api import API_Key
from flask import Flask, render_template,redirect,url_for,flash

app = Flask(__name__)

def data():
    city_name= 'New Delhi'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_Key}&units=metric'
    return url,city_name



def daily_forecast(weather_url,city):
    # url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_Key}&units=metric'
    
    response = requests.get(weather_url)
    data = response.json()
    print(data)
    
    daily_forecast = {}
    
    for item in data['list']:
        date = item['dt_txt'].split(' ')[0]
        temp = item['main']['temp']
        descreption = item['weather'][0]['description']
        humidity = item['main']['humidity']
        wind = item['wind']['speed']
        icon_code = item['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        
        today = datetime.now()
        f_today = today.strftime('%Y-%m-%d')
        day = today.day
        month = today.strftime('%B')
        year = today.year
        weekday = today.strftime('%A')
        print(today)
        
        if date not in daily_forecast:
            daily_forecast[date] = {
                "temp": temp,
                "description": descreption,
                "humidity": humidity,
                "wind": wind,
                "place" : city,
                "day" : day,
                "month" : month,
                "year" : year,
                "weekday" : weekday,
                "icon_url": icon_url
                
            }
      
        
        today_forcast ={}
        
        for date, forecast in daily_forecast.items():
            if date == f_today:
                today_forcast = forecast
                break 
    
    return today_forcast


def weekly_forcast(weather_url):
    # url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_Key}&units=metric'
    
    response = requests.get(weather_url)
    data = response.json()
    print(data)
    
    forecast_list = []
    
    if response.status_code == 200:
        for forecast in data['list']:
            dt_txt = forecast['dt_txt']  
            dt_obj = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            
            
            if dt_obj.hour == 12:
                day_name = dt_obj.strftime("%A")  
                temperature = forecast['main']['temp']
                description = forecast['weather'][0]['description']
                icon_code = forecast['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

                forecast_list.append({
                    "day": day_name,
                    "temperature": temperature,
                    "description": description,
                    "icon_url": icon_url
                })
    return forecast_list

@app.route('/')
def index():
    weather_url,city = data()
    forecast = daily_forecast(weather_url,city)
    weekly_forecast = weekly_forcast(weather_url)
    return render_template('index.html',forecast=forecast,weekly_forcast=weekly_forecast)





# @app.route('/')
# def index():
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         print('Weather is ', data['weather'][0]['description'])
#         print('Current Temperature is ',data['main']['temp'])
#         print('Current Temperature feels like ',data['main']['feels_like'])
#         print('Current humidity is ',data['main']['humidity'])
#         print('Current humidity is ',data['name'])
#         return render_template('index.html',datas=data)

if __name__ == '__main__':
    app.run(debug=True)
 
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print('Weather is ', data['weather'][0]['description'])
#     print('Current Temperature is ',data['main']['temp'])
#     print('Current Temperature feels like ',data['main']['feels_like'])
#     print('Current humidity is ',data['main']['humidity'])




