import folium
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'website/privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super(PrivacyPolicyView, self).get_context_data(**kwargs)
        return context


class BlogsView(TemplateView):
    template_name = 'website/blogs.html'

    def get_context_data(self, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        return context


class BlogDetailView(TemplateView):
    template_name = 'website/blog-details.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        return context


class ContactUsView(TemplateView):
    template_name = 'website/contact-us.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        marks = folium.Map(location=[45.5236, -122.6750], zoom_start=6)
        co_ordinates = (45.5236, -122.6750)
        folium.Marker(co_ordinates, popup=str("name")).add_to(marks)
        context['map'] = marks._repr_html_()

        return context
