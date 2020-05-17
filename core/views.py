import datetime

import requests
from django.shortcuts import render

# Create your views here.


def home(request):

    message = 'You should take an umbrella in these days: '

    response = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?id=3451328&appid=87ce1ae01bc818dcdfacf27b08b9695f'
    )
    data = response.json()

    humidity_list = []
    current_date = datetime.datetime.now().date()

    for forecast in data['list']:
        date = datetime.datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
        if date > current_date:
            if forecast['main']['humidity'] > 70:
                humidity_list.append(date.strftime("%A"))

    humidity_list = list(dict.fromkeys(humidity_list))

    return render(request, 'home.html', {
        'city_name': data['city']['name'],
        'list': humidity_list
    })
