# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')
