import folium
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView

from src.website.bll import get_or_create_website
from src.website.models import Blog


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['content'] = get_or_create_website()
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'website/privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super(PrivacyPolicyView, self).get_context_data(**kwargs)
        context['content'] = get_or_create_website()
        return context


class BlogsView(ListView):
    template_name = 'website/blogs.html'
    queryset = Blog.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        context['content'] = get_or_create_website()
        return context


class BlogDetailView(DetailView):
    template_name = 'website/blog-details.html'
    model = Blog

    def get_object(self, queryset=None):
        return get_object_or_404(Blog, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['content'] = get_or_create_website()
        return context


class ContactUsView(TemplateView):
    template_name = 'website/contact-us.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        context['content'] = get_or_create_website()
        return context
