from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registrationform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content',]