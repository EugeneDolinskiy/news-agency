from django.contrib.auth import get_user_model
from django.test import TestCase

from news_management.models import Topic, Newspaper


class ModelTests(TestCase):
    def test_topic_str(self):
        """
        Test that topic str representation works correctly
        """
        topic = Topic.objects.create(
            name="TestTopicName",
        )

        self.assertEqual(str(topic), topic.name)

    def test_redactor_str(self):
        """
        Test that redactor str representation works correctly
        """
        redactor = get_user_model().objects.create_user(
            username="TestUser", password="test123", years_of_experience=5
        )

        self.assertEqual(str(redactor), redactor.username)

    def test_redactor_create_with_experience(self):
        """
        Test that redactor creation with years of experience works correctly
        """
        username = "TestUser1"
        password = "test123"
        years_of_experience = 10
        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )

        self.assertEqual(redactor.username, username)
        self.assertEqual(redactor.years_of_experience, years_of_experience)
        self.assertTrue(redactor.check_password(password))

    def test_newspaper_str(self):
        """
        Test that newspaper str representation works correctly
        """
        topic = Topic.objects.create(name="TestTopicName")

        redactor = get_user_model().objects.create_user(
            username="TestUser", password="test123", years_of_experience=5
        )

        newspaper = Newspaper.objects.create(
            title="TestTitle", content="TestContent", topic=topic
        )
        newspaper.publishers.set([redactor])

        self.assertEqual(str(newspaper), newspaper.title)
