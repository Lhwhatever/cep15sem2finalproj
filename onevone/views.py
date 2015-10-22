from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from . import models, forms
from .forms import MatchForm

# Create your views here.
import acc
from cep15sem2finalproj import common
from cep15sem2finalproj.common.views import redirect_with_msg


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


class MatchCreateView(common.views.TemplateView):
    model = models.Match
    login_required = True
    template_name = "match_form.html"

    location_form = forms.LocationForm
    match_form = forms.MatchForm
    blacklist = True

    def get(self, request, *args, **kwargs):
        kwargs.setdefault('location_form', self.location_form())
        kwargs.setdefault('match_form', self.match_form())
        return super(MatchCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        location_form = self.location_form(data=request.POST)
        match_form = self.match_form(data=request.POST)

        if location_form.is_valid() and match_form.is_valid():
            location = location_form.save()
            match = match_form.save(commit=False)
            match.owner = acc.models.UserProfile.get(self.request.user)
            match.location = location
            match.save()

            return redirect_with_msg(request, 'Match created.', reverse_lazy('match.index'))
                                                                             


class MatchUpdateView(common.views.TemplateView):
    model = models.Match
    login_required = True
    template_name = "match_form.html"

    location_form = forms.LocationForm
    match_form = forms.MatchForm
    blacklist = True

    def get(self, request, *args, **kwargs):
        l = self.location_form(instance=models.Location.objects.get(pk=self.kwargs['pk']))
        m = self.match_form(instance=models.Match.objects.get(pk=self.kwargs['pk']))
        kwargs.setdefault('location_form', l)
        kwargs.setdefault('match_form', m)
        return super(MatchUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        location_form = self.location_form(data=request.POST, instance=models.Location.objects.get(pk=self.kwargs['pk']))
        match_form = self.match_form(data=request.POST, instance=models.Match.objects.get(pk=self.kwargs['pk']))

        if location_form.is_valid() and match_form.is_valid():
            location = location_form.save()
            match = match_form.save(commit=False)
            match.owner = acc.models.UserProfile.get(self.request.user)
            match.location = location
            match.save()
            match_form.save_m2m()

            return redirect_with_msg(request, 'Match updated.', reverse_lazy('match.index'))


class MatchDeleteView(common.views.DeleteView):
    model = models.Match
    login_required = True
    template_name = "delete_form.html"
    success_url = "/match/"


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
