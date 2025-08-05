from django.urls import path
from .views import home, about, contact, SimpleClassView, user_profile, home_template

urlpatterns = [
    path("", home, name="home"),
    path('sobre/', about, name="about"),
    path('contato/', contact, name="contact"),
    path('cbv/', SimpleClassView.as_view(), name="cbv"),
    path('user/<int:id>', user_profile, name="user_profile"),
    path('home/', home_template, name="home_template")
]
