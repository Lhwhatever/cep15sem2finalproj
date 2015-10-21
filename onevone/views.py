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


class MatchDetailView(common.views.TemplateView):
    template_name = "match_details.html"

    def update_context(self, **kwargs):
        hash_id = kwargs.get('hashcode')
        self.context.update('object', models.Match.objects.get(hash_id=hash_id))
