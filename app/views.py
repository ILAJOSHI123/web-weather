from django.shortcuts import render
import requests


# Create your views here.
<<<<<<< HEAD
def Index(request):
=======
def index(request):
>>>>>>> a312abb7bf23b0b2f2fa3680d530ac5248d3b172


    city =  request.GET.get('city',"Dehradun")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=be36e97843bb29fa55c0b8309c0b8ef9'
    data = requests.get(url).json()

    payload = {
        'city': data['name'], 
        'weather': data['weather'][0]['main'], 
        'icon': data['weather'][0]['icon'], 
        'kelvin_temperature' : data['main']['temp'],
        'celsius_temperature' : int(data['main']['temp']-273),
        'fahrenheit_temperature' : int(((data['main']['temp']-273.15)* 9/5  + 32)), 
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'], 
    }

    context = {'data': payload }
    print(context)
    return render(request, "app/index.html" , context)

