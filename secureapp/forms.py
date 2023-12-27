from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User\

# Captcha
from captcha.fields import ReCaptchaField


# Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    captcha = ReCaptchaField()



