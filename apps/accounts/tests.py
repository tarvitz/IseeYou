# coding: utf-8
#from django.utils import unittest

from django.test import TestCase
#from django.contrib.formtools.tests.wizard.wizardtests.tests import WizardTests
#from django.contrib.auth.models import User
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from apps.core.helpers import get_object_or_None
from apps.core.tests import TestHelperMixin
from django.utils.translation import ugettext_lazy as _

#from copy import deepcopy
#import simplejson as json
from decimal import Decimal


class ImplementMe(Exception):
    pass


class JustTest(TestCase):
    fixtures = [
        'tests/fixtures/load_users.json',
    ]

    def setUp(self):
        self.urls_void = [
        ]
        self.urls_registered = [
        ]
        self.get_object = get_object_or_None

    def test_registered_urls(self):
        messages = []
        for user in ('admin', 'user'):
            logged = self.client.login(username=user, password='123456')
            self.assertEqual(logged, True)
            for url in self.urls_registered:
                response = self.client.get(url, follow=True)
                try:
                    self.assertEqual(response.status_code, 200)
                except AssertionError as err:
                    messages.append({
                        'user': user, 'err': err, 'url': url
                    })
        if messages:
            for msg in messages:
                print "Got assertion on %(url)s with %(user)s: %(err)s" % msg
            raise AssertionError

    def tearDown(self):
        pass

    def check_state(self, instance, data, check=lambda x: x):
        messages = []
        for (key, value) in data.items():
            try:
                check(getattr(instance, key), value)
            except AssertionError as err:
                messages.append({
                    'err': err,
                    'key': key
                })
        if messages:
            for msg in messages:
                print "Got %(err)s in %(key)s" % msg
            raise AssertionError

    def test_login(self):
        login = {
            'username': 'user',
            'password': '123456'
        }
        url = reverse('accounts:login')
        response = self.client.post(url, login, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/logout/')

    def test_logout(self):
        pass

    def test_password_change(self):
        pass

    def test_password_recover(self):
        pass

    def test_profile_update(self):
        pass

    def test_register(self):
        pass
