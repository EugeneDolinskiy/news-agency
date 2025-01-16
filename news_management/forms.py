from django import forms
from django.contrib.auth.forms import UserCreationForm

from news_management.models import Redactor


class RedactorCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "username",
            "years_of_experience",
        )
