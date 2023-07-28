from django.shortcuts import render
from django.http import request,HttpResponse
import requests

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fe6ee3090dc5b0869d21813a6c8c86c5'
        response = requests.get(url)
        data = dict(response.json())
        return render(request,'weather.html',{
            'city':data['name'],
            'main':data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'max':data['main']['temp_max'],
            'min':data['main']['temp_min'],
            'feels':data['main']['feels_like'],
            })
    return render(request,'index.html',{})
