from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.views.generic import TemplateView
from core.settings import ENVIRONMENT


def handler404(request, *args, **kwargs):
    return render(request, "404.html")


def handler500(request, *args, **kwargs):
    return render(request, "500.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.website.urls', namespace='website')),

    # path('accounts/', include('allauth.urls')),
    # path('accounts/', include('src.accounts.urls', namespace='accounts')),
]

# universal urls
urlpatterns += [
    path('under-construction/', TemplateView.as_view(template_name='under-construction.html')),
    path('404/', TemplateView.as_view(template_name='404.html')),  # use: for page 404
    path('500/', TemplateView.as_view(template_name='500.html')),  # use: for page 500
]

if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
