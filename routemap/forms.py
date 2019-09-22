from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, EmailValidator
from django.forms import ModelForm

from routemap.models import Route, PhotoSpots, RouteList


class AddUserForm(ModelForm):
    password_repeated = forms.CharField(label="powtórz hasło", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_repeated = cleaned_data.get("password_repeated")
        print(password)
        print(password_repeated)

        if password != password_repeated:
            raise forms.ValidationError(
                "Hasła nie pasują!"
            )

    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets = {"password": forms.PasswordInput}


class LoginForm(forms.Form):
    login = forms.CharField(label="Login:")
    password = forms.CharField(label="Password:",
                               widget=forms.PasswordInput)


def validate_rating(rating):
    if not (1 <= float(rating) <= 6):
        raise ValidationError("Ocena musi być z zakresu 1-6")


class AddRouteForm(ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        surface_condition = cleaned_data.get("surface_condition")
        scenic_rating = cleaned_data.get("scenic_rating")
        funny_to_drive = cleaned_data.get("funny_to_drive")
        validate_rating(surface_condition)
        validate_rating(scenic_rating)
        validate_rating(funny_to_drive)

    class Meta:
        model = Route
        fields = ["starts", "ends", "country", "region", "description",
                  "surface_condition", "scenic_rating", "funny_to_drive",
                  "overal_rating", "embed_view"]


class AddSpotForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["photo_path"].widget.attrs.update({"class": "submit_btn"})

    class Meta:
        model = PhotoSpots
        fields = "__all__"


class AddListForm(ModelForm):

    class Meta:
        model = RouteList
        fields = ["name"]
