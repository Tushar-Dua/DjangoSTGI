from django.urls import path
from .import views

urlpatterns = [
    path("",views.landing),
    path("/all_blogs",views.blogs)
]