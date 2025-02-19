from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin123"
        )

        self.client.force_login(self.admin_user)

        self.redactor = get_user_model().objects.create_user(
            username="test_user", password="test123", years_of_experience=5
        )

    def test_redactor_years_of_experience_listed(self):
        """
        Test that redactor's years of experience is in list_display
        on redactor admin page
        :return:
        """
        url = reverse("admin:news_management_redactor_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_years_of_experience_listed(self):
        """
        Test that redactor's years of experience is on redactor detail admin
        page
        :return:
        """
        url = reverse(
            "admin:news_management_redactor_change", args=[self.redactor.id]
        )
        res = self.client.get(url)

        self.assertContains(res, self.redactor.years_of_experience)
