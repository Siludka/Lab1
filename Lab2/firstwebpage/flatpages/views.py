from django.shortcuts import render
from django import template

def handler(request):
    return render(request, 'static_handler.html')

# Create your views here.
