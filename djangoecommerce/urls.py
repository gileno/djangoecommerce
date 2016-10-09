from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.contrib.auth.views import login, logout

from core import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^admin/', admin.site.urls),
]
