from django.urls import path
from . import views

urlpatterns = [
    path('', HomeView.as_view, name="home"),
]