from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        ordering = ("-years_of_experience", )

    def __str__(self):
        return self.username


class Topic(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor)

    class Meta:
        ordering = ("title", "published_date")

    def __str__(self):
        return self.title
