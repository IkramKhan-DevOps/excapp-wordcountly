from django.shortcuts import render
from django.views.generic import TemplateView

from src.website.forms import EditorForm


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = EditorForm()
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'website/home.html'


class EmbedCodeView(TemplateView):
    template_name = 'website/home.html'