from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path("", home, name="home"),
    path('sobre/', about, name="about"),
    path('contato/', contact, name="contact")
]
