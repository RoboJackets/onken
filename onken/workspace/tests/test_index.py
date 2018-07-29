from django.shortcuts import reverse
from onken.workspace.test import WorkspaceTestCase
from django.contrib.auth import get_user_model


class IndexTest(WorkspaceTestCase):
    def test_index(self):
        User = get_user_model()
        user = User(username='gburdell3', first_name='George')
        user.save()

        self.client.force_login(user)

        response = self.client.get(reverse('workspace_index'))
        self.assertContains(response, "This is the workspace app.", status_code=200)
