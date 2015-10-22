from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ('status',)

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(UserProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = False
        return self.cleaned_data


class ComposeForm(ModelForm):
    class Meta:
        model = models.Messages
        fields = '__all__'
        widgets = {
            'sender': forms.Select(attrs={'readonly': True})
        }
    
    def full_clean(self):#http://stackoverflow.com/questions/4340287/override-data-validation-on-one-django-form-element
        super(ComposeForm, self).full_clean()
        if 'sender' in self._errors:
            self.cleaned_data['sender'] = []
            print("remove sender errors")
            del self._errors['sender']
