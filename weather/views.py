from django.shortcuts import render

import requests
from django.shortcuts import render
from django.conf import settings


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Kyiv&units=metric&appid=55f4e4cea012be98116ee8444789ef6e'
    response = requests.get(url)
    weather = response.json()
    return render(request, 'weather/home.html', {'weather': weather})
