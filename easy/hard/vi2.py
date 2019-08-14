from django.shortcuts import render
from django.http import HttpResponse


def ind2(request):
    return render(request, "2dop.html")