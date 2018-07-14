from onken.public.models import Workspace, Domain
from django.conf import settings
from django.test import TestCase, Client, override_settings

@override_settings(ROOT_URLCONF=settings.PUBLIC_SCHEMA_URLCONF)
class PublicTestCase(TestCase):
    def setUp(self):
        super(PublicTestCase, self).setUp()
        tenant = Workspace(schema_name='public')
        tenant.save()
        domain = Domain(tenant=tenant, domain="test.com")
        domain.save()
        self.client = Client(SERVER_NAME="test.com")
