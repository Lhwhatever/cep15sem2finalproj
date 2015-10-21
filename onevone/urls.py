from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',

    url(r'^match/l*$', views.MatchListView.as_view(), name='match.index'),
    #url(r'^match/d/(?P<hashcode>[a-zA-Z0-9+/])$', views.MatchDetailView.as_view()),
    url(r'^match/l/(?P<filter>\w+)$', views.MatchListView.as_view(), name='match.filtered'),
    url(r'^match/d/(?P<pk>\d+)$', views.MatchDetailView.as_view(), name='match.detail'),
    
    url(r'^match/l/c/$', views.MatchCreateView.as_view(), name='match.create'),
)

