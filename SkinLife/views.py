from django.http.response import HttpResponse
from django.shortcuts import  render


def sample(request):
    return render(request, 'SkinLife/home.html')
