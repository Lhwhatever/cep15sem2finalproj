from django.contrib import auth
from django.contrib.auth import views as authviews, authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from . import models

# Create your views here.
from django.views import generic
from cep15sem2finalproj import common
from cep15sem2finalproj.common.views import redirect_with_msg
from . import forms


class LoginView(common.views.FormView):

    template_name = 'loginpage.html'

    def dispatch(self, request, *args, **kwargs):
        return redirect_with_msg(request, 'You are already logged in.', 'home', permanent=False, *args, **kwargs) \
            if request.user.is_authenticated() else authviews.login(request, template_name='loginpage.html', extra_context={'user': models.UserProfile.get(self.request.user)})


class LogoutView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['Message'] = 'Logged out successfully.' if request.user.is_authenticated() else None

        return authviews.logout(request, next_page='/') if request.user.is_authenticated()\
            else redirect_with_msg(request, 'You are already logged out.', 'home')


class RelogView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['Message'] = 'Logged '


class RegisterView(generic.TemplateView):
    template_name = 'registration.html'
    app = 'home'

    user_form = forms.UserForm
    profile_form = forms.UserProfileForm

    def get(self, request, *args, **kwargs):
        kwargs.setdefault('user_form', self.user_form())
        kwargs.setdefault('profile_form', self.profile_form())
        return super(RegisterView, self).get(request, *args, app='home', **kwargs)

    def post(self, request, *args, **kwargs):
        user_form = self.user_form(data=request.POST)
        profile_form = self.profile_form(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            u = user_form.save()
            p = profile_form.save(commit=False)
            p.user = u
            p.save()
            
            """

            user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password1'))
            login(request, user)
            """
            return redirect_with_msg(request, 'Welcome!', 'home')

        else:
            return redirect_with_msg(
                request, 'The following errors were found: \n{0}'.format(user_form.errors), reverse_lazy('register')
            )


class ProfileView(common.views.DetailView):
    template_name = "profilepage.html"


class InboxView(common.views.ListView):
    model = models.Messages
    template_name = "inbox.html"

    def get_queryset(self):
        return self.model.objects.filter(recipient__id=models.UserProfile.get(self.request.user).id).order_by('-sent')


class ComposeView(common.views.TemplateView):
    model = models.Messages
    template_name = "compose.html"
    message_form = forms.ComposeForm

    def get(self, request, *args, **kwargs):
        initialize = {
            'sender': models.UserProfile.get(request.user)
        }
        
        recipient = request.GET.get('sendto', None)
        if recipient:
            initialize['recipient'] = models.UserProfile.objects.get(id=recipient)
            
        preset = request.GET.get('preset', None)
        if preset == 'askfor':
            import onevone.models
            match_id = request.GET.get('id')
            title = onevone.models.Match.objects.get(id=match_id).name
            
            initialize['subject'] = 'Request to join match: {0!s}'.format(title)
            initialize['content'] = 'Hello, I would like to join the match <a href="/match/d/{0!s}">{1!s}</a>.'.format(match_id, title)
            
        kwargs.setdefault('form', self.message_form(initial=initialize))
        return super(ComposeView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        post = {
            'subject': request.POST.get('subject'),
            'content': request.POST.get('content'),
            'recipient': request.POST.get('recipient'),
            'sender': str(models.UserProfile.get(request.user).id)
        }
        msg_form = self.message_form(post)
        if msg_form.is_valid():
            msg = msg_form.save(commit=False)
            print(msg)
            msg.save()
            return redirect_with_msg(request, 'Message sent.', reverse_lazy('home'))
        else:
            print(msg_form.errors)
            return redirect_with_msg(
                request, 'The following errors were found: \n{0}'.format(msg_form.errors),
                reverse_lazy('compose')
            )
