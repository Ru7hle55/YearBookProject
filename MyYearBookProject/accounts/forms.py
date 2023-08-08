from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from MyYearBookProject.accounts.models import ProjectUser


class ProjectUserCreateForm(UserCreationForm):
    class Meta:
        model = ProjectUser
        fields = (
            'username',
            'email',
        )


class ProjectUserEdirForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile_picture',
            'gender',
        )
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Image',
            'gender': 'Gender',
        }


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Password',
            }
        )
    )
