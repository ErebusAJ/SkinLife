from django.shortcuts import render
from django.http.response import responses


def home(request):
    return render(request, 'skin_app/home.html')
