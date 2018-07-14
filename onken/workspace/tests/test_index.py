from django.shortcuts import reverse
from django.conf import settings
from onken.workspace.test import WorkspaceTestCase


class IndexTest(WorkspaceTestCase):
    def test_index(self):
        response = self.client.get(reverse('workspace_index'))
        self.assertContains(response, "This is the workspace app.", status_code=200)
