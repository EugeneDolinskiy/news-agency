from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from news_management.models import Redactor, Newspaper


class RedactorCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "username",
            "years_of_experience",
        )


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    published_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title"
            }
        )
    )
