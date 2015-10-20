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

    def save(self, commit=True):
        u = models.UserProfile.get(self.user)
        u.status = self.cleaned_data.get('status')
        u.save()
        return u
