from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("user/", views.user, name="user"),
    path("group/", views.group, name="group"),
    path("<int:id>/", views.edit, name="edit"),
    #path("<int:id>/", views.activate, name="activate")
]
