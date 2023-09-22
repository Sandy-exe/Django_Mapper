from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.
def index(request):
    # def weather(request, city):
    #     url = 'https://api-client.imei.org/api/dhru'
    #     key ='KkODHlJq1PyI38BmCvDBW21qFRXrqQOh0aJx9sYJYtHpvdx9dhmIl76KLjyO'
    #     url = 'http://api-client.imei.org/api/services?apikey={'+key+'}'.format(city)
    #     response = requests.get(url)
    #     data = response.json()
    #     return JsonResponse(data)
    key ='KkODHlJq1PyI38BmCvDBW21qFRXrqQOh0aJx9sYJYtHpvdx9dhmIl76KLjyO'
    url1 = 'http://api-client.imei.org/api/submit?apikey={}&service_id={}&input={}'.format(key,17,356131100146516)
    response = requests.get(url1)
    print(response)
    data = response.json()
    print(data)
    return render(request,'index.html')