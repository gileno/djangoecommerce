# coding=utf-8

from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import User
from .forms import UserAdminCreationForm


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


register = RegisterView.as_view()
