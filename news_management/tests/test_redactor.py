from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


REDACTOR_LIST_URL = reverse("news_management:redactor-list")
REDACTOR_CREATE_URL = reverse("news_management:redactor-create")


class PublicRedactorTests(TestCase):
    def test_login_required(self):
        """Test that login is required to access the redactor list view"""
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self):
        """Set up a logged-in user and test data"""
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
        )
        self.client.force_login(self.user)

        self.redactor = get_user_model().objects.create_user(
            username="redactor1",
            password="password123",
            years_of_experience=5,
            first_name="John",
            last_name="Doe",
        )

    def test_retrieve_redactor_list(self):
        """Test retrieving the list of redactors"""
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.redactor, response.context["redactor_list"])
        self.assertTemplateUsed(response, "news_management/redactor_list.html")

    def test_search_redactor_by_username(self):
        """Test searching redactors by username"""
        get_user_model().objects.create_user(
            username="redactor2",
            password="password123",
            years_of_experience=10,
        )
        response = self.client.get(REDACTOR_LIST_URL, {"username": "redactor1"})
        self.assertEqual(len(response.context["redactor_list"]), 1)
        self.assertEqual(response.context["redactor_list"][0], self.redactor)

    def test_retrieve_redactor_detail(self):
        """Test retrieving a redactor's detail view"""
        url = redactor_detail_url(self.redactor.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["redactor"], self.redactor)
        self.assertTemplateUsed(response, "news_management/redactor_detail.html")

    def test_create_redactor(self):
        """Test creating a new redactor"""
        form_data = {
            "username": "new_redactor",
            "password1": "Strongpassword123",
            "password2": "Strongpassword123",
            "years_of_experience": 3,
            "first_name": "Jane",
            "last_name": "Smith",
        }
        response = self.client.post(REDACTOR_CREATE_URL, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            get_user_model().objects.filter(username="new_redactor").exists()
        )

    def test_update_redactor(self):
        """Test updating redactor"""
        form_data = {
            "username": "new_redactor",
            "password1": "Strongpassword123",
            "password2": "Strongpassword123",
            "years_of_experience": 3,
            "first_name": "Jane",
            "last_name": "Smith",
        }
        url = redactor_update_url(self.redactor.id)
        response = self.client.post(url, data=form_data)
        self.redactor.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.redactor.username, form_data["username"])


def redactor_detail_url(pk):
    return reverse("news_management:redactor-detail", args=[pk])


def redactor_update_url(pk):
    return reverse("news_management:redactor-update", args=[pk])
