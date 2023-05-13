from django.shortcuts import render
import requests


def home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    json_response = response.json()
    return render(request, 'products.html', {'data': json_response})