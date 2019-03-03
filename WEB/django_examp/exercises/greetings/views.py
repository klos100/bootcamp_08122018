from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def hello_world(request):
    return HttpResponse("Hello World")

def hello_name(request,name):
    return HttpResponse(f"Hello {name}")