from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('men', views.men, name="men"),
    path('collections', views.collections, name="collections"),


]