from django.shortcuts import render
import requests
import json

def get_weather_data(city):
    api_key = 'f4ebc0c3e6f9a5657643d2cbd5966c06'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = json.loads(response.text)

    results = {}

    results['area'] = data.get('name')
    results['weather'] = data.get('weather')[0].get('description')
    results['temp'] = data.get('main').get('temp')
    results['feels_like'] = data.get('main').get('feels_like')

    return results


# Create your views here.
def home_view(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST.get('city')
        results = get_weather_data(city)
        context = {'results': results}
    else:
        context = {}

    return render(request, 'weather/home.html', context)

