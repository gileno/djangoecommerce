# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def product_list(request):
    return render(request, 'product_list.html')


def product(request):
    return render(request, 'product.html')
