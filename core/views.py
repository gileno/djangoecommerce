# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
