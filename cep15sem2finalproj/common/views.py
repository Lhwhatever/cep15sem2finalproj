from django.views import generic


class TemplateView(generic.TemplateView):
    """
    Generic template view file. Use this.
    """

    context = {}

    login_required = False
    whitelist = False
    users = ()

    def update_context(self):
        pass

    def get_context_data(self, **kwargs):
        self.update_context()
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context.update(self.context)
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.login_required and ((request.user in self.users) ^ self.whitelist):
            return super(TemplateView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponse
