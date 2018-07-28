from django.shortcuts import reverse
from onken.public.models import User
from onken.public.test import PublicTestCase


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
            reverse('admin:public_workspace_delete', args=(2,))
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

    def test_non_staff_dont_loop_admin_login(self):
        user = User.objects.create_user(
            username='gburdell3',
            email='george.burdell@gatech.edu',
            password='THWg'
        )

        self.client.force_login(user)

        response = self.client.get(reverse('admin:index'), follow=True)

        self.assertEqual(response.status_code, 403)

    def test_staff_clears_admin_login(self):
        user = User.objects.create_superuser(
            username='gburdell3',
            email='george.burdell@gatech.edu',
            password='THWg'
        )

        self.client.force_login(user)

        response = self.client.get(reverse('admin:index'), follow=True)

        self.assertEqual(response.status_code, 200)

    def test_anon_cant_admin_login(self):
        response = self.client.get(reverse('admin:login'), follow=False)

        self.assertRedirects(
            response,
            'http://localhost:3004/login?service=http%3A%2F%2Ftest.com%2Fadmin%2Flogin%2F%3Fnext%3D%252F',
            status_code=302,
            fetch_redirect_response=False
        )
