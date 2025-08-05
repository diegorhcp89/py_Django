from django.urls import path
from .views import home, about, contact, SimpleClassView

urlpatterns = [
    path("", home, name="home"),
    path('sobre/', about, name="about"),
    path('contato/', contact, name="contact"),
    path('cbv/', SimpleClassView.as_view(), name="cbv")
]
