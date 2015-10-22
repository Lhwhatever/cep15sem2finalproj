from django.shortcuts import render
from . import models, forms

# Create your views here.
from cep15sem2finalproj import common


class MatchListView(common.views.ListView):
    model = models.Match
    template_name = "object_list.html"

    def get_queryset(self):
        list_filter = self.kwargs.get('filter', None)
        return self.model.objects.filter(category__label=list_filter, privacy__gt=0) if list_filter \
            else self.model.objects.filter(privacy__gt=0)
            
    def update_context(self, **kwargs):
        self.context['filter'] = self.kwargs.get('filter', None)
        self.context['type'] = 'match'


class MatchDetailView(common.views.DetailView):
    template_name = "match_details.html"
    model = models.Match


class MatchCreateView(common.views.CreateView):
    form_class = forms.MatchForm
    model = models.Match
    login_required = True
    set_default_user = True
    template_name = "match_form.html"
    success_url = 'match.index'


class TourneyListView(common.views.ListView):
    model = models.Tournament
    template_name = "object_list.html"

    def get_queryset(self):
        list_filter = self.kwargs.get('filter', None)
        return self.model.objects.filter(category__label=list_filter, privacy__gt=0) if list_filter\
            else self.model.objects.filter(privacy__gt=0)

    def update_context(self):
        self.context['filter'] = self.kwargs.get('filter', None)
        self.context['type'] = 'tourney'


class TourneyDetailView(common.views.DetailView):
    template_name = "tourney_details.html"
    model = models.Tournament
