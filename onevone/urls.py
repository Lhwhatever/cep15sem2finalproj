from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',

    url(r'^match/$', views.MatchListView.as_view()),
    url(r'^match/d/(?P<hashcode>[a-zA-Z0-9+/])$', views.MatchDetailView.as_view()),

    url(r'^event/$', views.EventView.as_view()),
    url(r'^ranking/$', views.RankingView.as_view()),
)

