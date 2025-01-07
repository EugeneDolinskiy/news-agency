from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=False, blank=False)

    class Meta:
        ordering = ("-years_of_experience", )

    def __str__(self):
        return self.username
