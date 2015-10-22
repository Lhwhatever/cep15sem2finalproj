from django import forms
from . import models


class LocationForm(forms.ModelForm):

    class Meta:
        model = models.Location
        fields = ('loc_name', 'full_text', 'is_online')

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields['loc_name'].label = 'Location Name'
        self.fields['full_text'].label = 'Location Description'
        self.fields['is_online'].label = 'Is location online?'


class MatchForm(forms.ModelForm):

    class Meta:
        model = models.Match
        fields = ('name', 'game', 'description', 'category', 'vacancies', 'time_start', 'time_end', 'privacy')
        widgets = {
            'time_start': forms.DateTimeInput(attrs={'class': 'datetimepicker', 'required': True}),
            'time_end': forms.DateTimeInput(attrs={'class': 'datetimepicker', 'required': True})
        }
