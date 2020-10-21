from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_user/", views.create_user, name="create_user"),
    path("create_group/", views.create_group, name="create_group"),
    path("user/", views.user, name="user"),
    path("group/", views.group, name="group"),
    path("<int:id>/", views.edit, name="edit"),
    #path("<int:id>/", views.activate, name="activate")
]
