from django.shortcuts import render
from . import models

# Create your views here.
from cep15sem2finalproj import common


class EventView(common.views.ListView):
    template_name = "eventpage.html"


class RankingView(common.views.ListView):
    template_name = "rankinglist.html"


class MatchListView(common.views.ListView):
    model = models.Match
    template_name = "match_list.html"

    def get_queryset(self):
        return self.model.objects.get(category__label=filter) if self.kwargs.get('filter', None) \
            else super(MatchListView, self).get_queryset()

    def update_context(self, **kwargs):
        self.context['filter'] = self.kwargs.get('filter', None)


class MatchDetailView(common.views.DetailView):
    template_name = "match_details.html"
    model = models.Match
