from django.conf import settings
from django.shortcuts import redirect
from django.views import generic
from acc import models


class TemplateView(generic.TemplateView):
    """
    Generic template view file.
    """

    context = {}

    login_required = False
    users = ()
    blacklist = True
    redirect = None

    def update_context(self):
        pass

    def get_context_data(self, **kwargs):
        self.update_context()
        self.context.update(kwargs)
        return super(TemplateView, self).get_context_data(user=models.UserProfile.get(self.request.user),
                                                          message=self.request.session.pop('message', None),
                                                          category=get_categories(),
                                                          **self.context)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(TemplateView, self).dispatch,
                                       message=None,
                                       redirect_to=self.redirect,
                                       enforce=self.login_required,
                                       users=self.users,
                                       blacklist=self.blacklist)


class ListView(generic.ListView):
    """
    Generic list view file.
    """

    context = {}

    login_required = False
    users = ()
    blacklist = True
    redirect = None

    def update_context(self):
        pass

    def get_context_data(self, **kwargs):
        self.update_context()
        self.context.update(kwargs)
        return super(ListView, self).get_context_data(user=models.UserProfile.get(self.request.user),
                                                      message=self.request.session.pop('message', None),
                                                      **self.context)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(ListView, self).dispatch,
                                       message=None,
                                       redirect_to=self.redirect,
                                       enforce=self.login_required,
                                       users=self.users,
                                       blacklist=self.blacklist)


class DetailView(generic.DetailView):
    """
    Generic detail view file
    """

    context = {}

    login_required = False
    users = ()
    blacklist = True
    redirect = None

    def update_context(self):
        pass

    def get_context_data(self, **kwargs):
        self.update_context()
        self.context.update(kwargs)
        return super(DetailView, self).get_context_data(user=models.UserProfile.get(self.request.user),
                                                        message=self.request.session.pop('message', None),
                                                        **self.context)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(DetailView, self).dispatch,
                                       message=None,
                                       redirect_to=self.redirect,
                                       enforce=self.login_required,
                                       users=self.users,
                                       blacklist=self.blacklist)


def redirect_with_msg(request, message, to, permanent=False, *args, **kwargs):
    request.session['message'] = message
    return redirect(to, permanent=permanent, *args, **kwargs)


def login_required_redirect(request, dispatch, message=None, redirect_to=None, enforce=True, users=(), blacklist=True,
                            *args, **kwargs):
    if ((not enforce) or request.user.is_authenticated()) and\
            ((models.UserProfile.get(request.user) in users) ^ blacklist):
        return dispatch(request, *args, **kwargs)
    else:
        return redirect_with_msg(request,
                                 message or 'This page is private.',
                                 redirect_to or settings.LOGIN_URL,
                                 *args, **kwargs)


class FormView(generic.FormView):
    context = {}

    login_required = False
    users = ()
    blacklist = True
    redirect = None

    def update_context(self):
        pass

    def get_context_data(self, **kwargs):
        self.update_context()
        self.context.update()
        return super(FormView, self).get_context_data(user=models.UserProfile.get(self.request.user),
                                                      message=self.request.session.pop('message', None),
                                                      **self.context)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(FormView, self).dispatch,
                                       message=None,
                                       redirect_to=self.redirect,
                                       enforce=self.login_required,
                                       users=self.users,
                                       blacklist=self.blacklist)
