from django.urls import path
from .views import (
    HomeView, PrivacyPolicyView, EmbedCodeView
)

app_name = "website"
urlpatterns = [

    path('', HomeView.as_view(), name='home')

]
