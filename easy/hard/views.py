from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return render(request, "base.html")
# Create your views here.