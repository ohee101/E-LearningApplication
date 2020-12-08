from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from App_Login.models import Instructor, Learner

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(
        required=True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    class Meta:
        model = User
        fields = ('username', 'password')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="",widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(
        required=True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        required=True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        exclude = ('user', )

class LearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        exclude = ('user', )