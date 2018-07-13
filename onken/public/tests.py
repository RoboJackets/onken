from django.shortcuts import reverse
from django.conf import settings
from onken.public.models import Workspace, Domain
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class IndexTest(TestCase):
    def setUp(self):
        super(IndexTest, self).setUp()
        tenant = Workspace(schema_name='public')
        tenant.save()
        domain = Domain(tenant=tenant, domain="test.com")
        domain.save()

    def test_index(self):
        user = User(username='gburdell3', first_name='George')
        user.save()
        client = Client(SERVER_NAME="test.com")
        client.force_login(user)
        response = client.get(reverse('public_index', urlconf=settings.PUBLIC_SCHEMA_URLCONF))
        self.assertContains(response, "This is the public app.", status_code=200)
