from django.contrib.auth import get_user_model

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields=('username','email', )

class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields=('username','email', )

