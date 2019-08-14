from django.shortcuts import render
from django.http import HttpResponse


def ind1(request):
    return render(request, "dop.html")