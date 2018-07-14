from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from onken.public.models import Workspace, Domain
from django.conf import settings


class WorkspaceTestCase(TenantTestCase):
    def setUp(self):
        super(WorkspaceTestCase, self).setUp()
        self.client = TenantClient(self.tenant)
