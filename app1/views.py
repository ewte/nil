from django.shortcuts import render
from django.http import HttpResponse
from . import service
from .models import MyModel

def index(request):
    return HttpResponse(service.model_worker())



