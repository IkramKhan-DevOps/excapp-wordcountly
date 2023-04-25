
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core.settings import ENVIRONMENT

# EXTERNAL APPS URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

# universal urls
urlpatterns += [
    path('under-construction/', TemplateView.as_view(template_name='under-construction.html')),
    path('404/', TemplateView.as_view(template_name='404.html')),  # use: for page 404
    path('500/', TemplateView.as_view(template_name='500.html')),  # use: for page 500
]

# your apps urls
urlpatterns += [
    path('', include('src.website.urls', namespace='website')),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
]

if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
