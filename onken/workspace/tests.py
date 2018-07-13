from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from django.shortcuts import reverse


class IndexTest(TenantTestCase):
    def setUp(self):
        super(IndexTest, self).setUp()
        self.c = TenantClient(self.tenant)

    def test_index(self):
        response = self.c.get(reverse('workspace_index'))
        self.assertContains(response, "This is the workspace app.", status_code=200)
