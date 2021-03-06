from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    """
    Форма регистрации пользователя: имя, почта, пароль.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
