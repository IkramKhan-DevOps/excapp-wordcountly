from django.urls import path
from .views import (
    HomeView, PrivacyPolicyView, BlogsView, ContactUsView
)

app_name = "website"
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),

]
