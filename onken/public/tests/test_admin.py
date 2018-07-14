from django.shortcuts import reverse
from django.contrib.auth.models import User
from onken.public.test import PublicTestCase
from onken.public.models import Workspace


class AdminTest(PublicTestCase):
    def test_admin_cant_delete_workspace(self):
        user = User.objects.create_superuser(
            username='gburdell3',
            email='george.burdell@gatech.edu',
            password='THWg'
        )

        self.client.force_login(user)

        response = self.client.get(reverse('admin:index'), follow=True)

        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('admin:public_workspace_delete', args=(2,)),
            #{'object_id': 2},
            #follow=True
        )

        self.assertEqual(response.status_code, 403)

    def test_admin_workspace_changelist_shows_names(self):
        user = User.objects.create_superuser(
            username='gburdell3',
            email='george.burdell@gatech.edu',
            password='THWg'
        )

        self.client.force_login(user)

        response = self.client.get(reverse('admin:index'), follow=True)

        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('admin:public_workspace_changelist'))

        # Note that the below assertions are dependent on implementation of the PublicTestCase
        self.assertContains(response, "The Public Tenant", status_code=200)
        self.assertContains(response, "test.com", status_code=200)


    def test_admin_domain_changelist_shows_names(self):
        user = User.objects.create_superuser(
            username='gburdell3',
            email='george.burdell@gatech.edu',
            password='THWg'
        )

        self.client.force_login(user)

        response = self.client.get(reverse('admin:index'), follow=True)

        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('admin:public_domain_changelist'))

        # Note that the below assertions are dependent on implementation of the PublicTestCase
        self.assertContains(response, "The Public Tenant", status_code=200)
        self.assertContains(response, "test.com", status_code=200)
