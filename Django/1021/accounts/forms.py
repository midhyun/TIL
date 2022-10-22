from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "gender",
            "genre",
            "image",
        )


class UserCustomChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
            "gender",
            "genre",
            "image",
        )


class UserCustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        pass
