from django.shortcuts import render, HttpResponse
import requests

add = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid=db5c29e52fe2ecea66121505640ad4c5'
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        add = f'api.openweathermap.org/data/2.5/weather?q={city}&appid=db5c29e52fe2ecea66121505640ad4c5'
        fin = "http://"+add
        context ={}
        jason = requests.get(fin).json()
        context['formatted']=jason['weather'][0]['description']
        return render(request, 'index.html',context)
    return render(request, 'index.html')
    