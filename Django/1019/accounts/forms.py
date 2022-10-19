from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )

class UserFormUpdate(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )