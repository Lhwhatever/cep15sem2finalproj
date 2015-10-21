from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',

    url(r'^match/$', views.MatchListView.as_view()),

    url(r'^event/$', views.EventView.as_view()),
    url(r'^ranking/$', views.RankingView.as_view()),
)

