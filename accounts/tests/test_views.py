# coding=utf-8

from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from accounts.models import User


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data = {
            'username': 'gileno', 'password1': 'teste123', 'password2': 'teste123',
            'email': 'test@test.com'
        }
        response = self.client.post(self.register_url, data)
        index_url = reverse('index')
        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)

    def test_register_error(self):
        data = {'username': 'gileno', 'password1': 'teste123', 'password2': 'teste123'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
