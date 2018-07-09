from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


class DummyTest(TestCase):
    def test_home_view(self):
        user = User.objects.create_user(username='gburdell3', first_name='George')

        client = Client()
        client.force_login(user)

        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "George")
