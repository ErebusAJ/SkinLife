from django.shortcuts import render


def dashboard(request):
    return render(request, template_name='model_prediction/diagnose.html')


