from django.contrib.auth.forms import UserCreationForm

from blog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        # exclude = ('created_at', 'updated_at')
        fields = ("email", "password1", "password2")