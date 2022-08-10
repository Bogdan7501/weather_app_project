import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=b1ec3d019abc164343b58ae5fc743b32'
    city = 'Kyiv'

    req = requests.get(url.format(city)).json()
    # print(req.text)
    city_weather = {
        'city': city,
        'temperature': req['main']['temp'],
        'description': req['weather'][0]['description'],
        'country_code': req['sys']['country'],
        'coordinate': req['coord']['lon'],
        'pressure': req['main']['pressure'],
        'humidity': req['main']['humidity'],
        'main': req['weather'][0]['main'],
        'icon': req['weather'][0]['icon'],
    }
    print(city_weather)
    context = {'city_weather': city_weather}
    return render(request,'main_app/index.html',context)