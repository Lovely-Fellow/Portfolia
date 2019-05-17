from django.conf import settings
from django.views.generic import TemplateView, CreateView

from .forms import SubscriberAddForm


class ThanksSignupView(TemplateView):
    template_name = 'account/thanks.html'


class SubscribeAddView(CreateView):
    template_name = 'account/index.html'
    success_url = '/thanks/'
    form_class = SubscriberAddForm

    def form_valid(self, form):
        print('here---------------')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('here error--------------')
        print(form.errors)
        return super().form_invalid(form)

