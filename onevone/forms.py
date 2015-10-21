from django import forms
from . import models


class MatchForm(forms.ModelForm):

    class Meta:
        model = models.Match
        fields = ('name', 'game', 'description', 'category', 'vacancies', 'time_start', 'time_end', 'privacy')
