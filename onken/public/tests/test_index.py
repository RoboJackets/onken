from django.shortcuts import reverse
from django.contrib.auth.models import User
from onken.public.test import PublicTestCase


class IndexTest(PublicTestCase):
    def test_index(self):
        user = User(username='gburdell3', first_name='George')
        user.save()

        self.client.force_login(user)

        response = self.client.get(reverse('public_index'))

        self.assertContains(response, "This is the public app.", status_code=200)
