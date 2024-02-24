from django import forms
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from sorl.thumbnail import ImageField
from django.db import models


class PostForm(forms.Form):
    text = forms.CharField()
    image = forms.FileField()


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )

class ProfileUpdateForm(forms.ModelForm):
    image= models.ImageField(upload_to='profiles', blank=True, null=True)
    class Meta:
        model = Profile
        fields = ['image']

