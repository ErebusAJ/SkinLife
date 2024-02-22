from django.shortcuts import render
from django.http.response import responses
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'skin_app/home.html')


@login_required()
def dashboard(request):
    return render(request, 'skin_app/main_app.html')
