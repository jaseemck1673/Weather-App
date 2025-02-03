from flask import Flask, render_template, request
from datetime import datetime
import requests
import requests

from api import API_Key


app = Flask(__name__)


def data():
    city_name = "New Delhi"  # Default city if no city is provided
    if request.method == 'POST':  # Only try to get city name from form if it's a POST request
        city_name = request.form.get('city')
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_Key}&units=metric'
    return url, city_name



def daily_forecast(weather_url,city): #today forecast details fetching function
    
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
        
        # daily forcasying is adding into daily_forecast dictionary
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
        # fecthing today forecast data 
        for date, forecast in daily_forecast.items():
            if date == f_today:
                today_forcast = forecast
                break 
    
    return today_forcast


def weekly_forcast(weather_url): #fetching weekly forcast details
    
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

@app.route('/',methods=['GET', 'POST'])
def index():
    weather_url,city = data()
    forecast = daily_forecast(weather_url,city)
    weekly_forecast = weekly_forcast(weather_url)
    return render_template('index.html',forecast=forecast,weekly_forcast=weekly_forecast)



if __name__ == '__main__':
    app.run(debug=True)
 
