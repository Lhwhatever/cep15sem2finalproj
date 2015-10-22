from django import forms
from . import models


class MatchForm(forms.ModelForm):

    class Meta:
        model = models.Match
        fields = ('name', 'game', 'description', 'category', 'vacancies', 'time_start', 'time_end', 'privacy')

def __init__(self, *args, **kwargs):
    super(NoteForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.form_id = "Matchform"
    tag = Div('tag',css_class = "col-xs-12", style="padding:0px;")