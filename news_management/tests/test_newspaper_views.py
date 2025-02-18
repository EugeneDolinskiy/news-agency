from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news_management.models import Topic, Newspaper

NEWSPAPER_LIST_URL = reverse("news_management:newspaper-list")
NEWSPAPER_CREATE_URL = reverse("news_management:newspaper-create")


class PublicNewspaperTests(TestCase):
    def test_login_required(self):
        """Test that login is required for accessing the newspaper list view"""
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateNewspaperTests(TestCase):
    def setUp(self):
        """Set up a logged-in user and sample data"""
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.force_login(self.user)

        self.topic = Topic.objects.create(
            name="TestTopic"
        )
        self.redactor = get_user_model().objects.create_user(
            username="redactor1",
            password="password123",
            years_of_experience=5,
        )
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test content",
            topic=self.topic
        )
        self.newspaper.publishers.add(self.redactor)

    def test_retrieve_newspaper_list(self):
        """Test retrieving the newspaper list"""
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.newspaper, response.context["newspaper_list"])
        self.assertTemplateUsed(
            response,
            "news_management/newspaper_list.html"
        )

    def test_search_newspaper_by_title(self):
        """Test searching newspapers by title"""
        response = self.client.get(
            NEWSPAPER_LIST_URL, {"title": self.newspaper.title}
        )
        self.assertEqual(len(response.context["newspaper_list"]), 1)
        self.assertEqual(response.context["newspaper_list"][0], self.newspaper)

    def test_retrieve_newspaper_detail(self):
        """Test retrieving the newspaper detail"""
        url = newspaper_detail_url(self.newspaper.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["newspaper"], self.newspaper)
        self.assertTemplateUsed(
            response, "news_management/newspaper_detail.html"
        )

    def test_create_newspaper(self):
        """Test creating a new newspaper"""
        from_data = {
            "title": "TestTitle",
            "content": "TestContent",
            "topic": self.topic.id,
            "publishers": [self.redactor.id]
        }
        response = self.client.post(NEWSPAPER_CREATE_URL, data=from_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Newspaper.objects.filter(title="TestTitle").exists())
        newspaper = Newspaper.objects.get(title="TestTitle")
        self.assertEqual(newspaper.topic, self.topic)
        self.assertIn(self.redactor, newspaper.publishers.all())

    def test_update_newspaper(self):
        """Test updating an existing newspaper"""
        new_redactor = get_user_model().objects.create_user(
            username="redactor3",
            password="password123",
            years_of_experience=10,
        )
        form_data = {
            "title": "TestTitle Updated",
            "content": "TestContent",
            "topic": self.topic.id,
            "publishers": [self.redactor.id, new_redactor.id]
        }
        url = newspaper_update_url(self.newspaper.id)
        response = self.client.post(url, data=form_data)
        self.newspaper.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.newspaper.title, "TestTitle Updated")
        self.assertIn(new_redactor, self.newspaper.publishers.all())

    def test_delete_newspaper(self):
        """Test deleting a newspaper"""
        url = newspaper_delete_url(self.newspaper.id)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Newspaper.objects.filter(id=self.newspaper.id).exists()
        )


def newspaper_detail_url(pk):
    return reverse("news_management:newspaper-detail", args=[pk])


def newspaper_update_url(pk):
    return reverse("news_management:newspaper-update", args=[pk])


def newspaper_delete_url(pk):
    return reverse("news_management:newspaper-delete", args=[pk])
