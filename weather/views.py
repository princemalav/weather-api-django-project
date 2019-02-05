from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=0383f126ef4c16ade5e9bfbc53c8aa3c'
    if request.method == 'POST':
        city = request.POST.get('city')
        print(city)
        r = requests.get(url.format(city)).json()
        #print(r)
        city_weather = {
            'city':city,
            'temprature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        #print(city_weather)
        context = {'city_weather':city_weather}
        return render(request,'weather/weather.html',context)
    return render(request,'weather/weather.html')
