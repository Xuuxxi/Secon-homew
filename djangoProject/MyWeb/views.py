from django.shortcuts import render
from django.http import HttpResponse


def sorry(request):
    return HttpResponse('Sorry bro')
