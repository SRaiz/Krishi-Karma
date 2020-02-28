from django.http import HttpResponse
from django.shortcuts import render

from .models import Crop


def index(request):
    crops = Crop.objects.all();
    return render(request, 'index.html', {'crops': crops})
