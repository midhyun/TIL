from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )
    
class ChangeUserForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', )