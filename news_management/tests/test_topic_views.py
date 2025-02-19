from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news_management.models import Topic

TOPIC_URL = reverse("news_management:topic-list")
TOPIC_CREATE_URL = reverse("news_management:topic-create")


class PublicTopicTests(TestCase):
    def test_login_required(self):
        response = self.client.get(TOPIC_URL)
        self.assertNotEqual(response.status_code, 200)

        response = self.client.get(TOPIC_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test123"
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(name="TestTopicName")

    def test_search_topic_by_name(self):
        """Test searching topic by name"""
        Topic.objects.create(
            name="TopicName",
        )
        response = self.client.get(TOPIC_URL, {"name": "TestTopicName"})
        self.assertEqual(len(response.context["topic_list"]), 1)
        self.assertEqual(response.context["topic_list"][0], self.topic)

    def test_retrieve_topic(self):
        Topic.objects.create(name="Test Topic 1")
        Topic.objects.create(name="Test Topic 2")
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(len(topics), 3)
        self.assertEqual(list(response.context["topic_list"]), list(topics))
        self.assertTemplateUsed(response, "news_management/topic_list.html")

    def test_create_topic(self):
        from_data = {
            "name": "New Topic",
        }
        response = self.client.post(TOPIC_CREATE_URL, from_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(name="New Topic").exists())

    def test_update_topic(self):
        update_url = topic_update_url(self.topic.id)
        form_data = {
            "name": "Updated Topic",
        }
        response = self.client.post(update_url, data=form_data)
        self.topic.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.topic.name, "Updated Topic")


def topic_update_url(pk):
    return reverse("news_management:topic-update", args=[pk])


def topic_delete_url(pk):
    return reverse("news_management:topic-delete", args=[pk])
