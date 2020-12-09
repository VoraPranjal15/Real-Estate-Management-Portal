from django_school.users.models import User
from django.test import TestCase
from django.contrib import auth

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('project', 'project', 'pass12345')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='project', password='pass12345')