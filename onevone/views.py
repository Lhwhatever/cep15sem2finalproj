from django.shortcuts import render
from . import models, forms

# Create your views here.
from cep15sem2finalproj import common


class MatchListView(common.views.ListView):
    model = models.Match
    template_name = "match_list.html"

    def get_queryset(self):
        list_filter = self.kwargs.get('filter', None)
        return self.model.objects.filter(category__label=list_filter, privacy__gt=0) if list_filter \
            else self.model.objects.filter(privacy__gt=0)
            
    def update_context(self, **kwargs):
        self.context['filter'] = self.kwargs.get('filter', None)


class MatchDetailView(common.views.DetailView):
    template_name = "match_details.html"
    model = models.Match


class MatchCreateView(common.views.CreateView):
    form_class = forms.MatchForm
    model = models.Match
    login_required = True
    set_default_user = True
    template_name = "match_form.html"

    def dispatch(self, request, *args, **kwargs):
        a = super(MatchCreateView, self).dispatch(request, *args, **kwargs)
        print(kwargs.form)
        return a
