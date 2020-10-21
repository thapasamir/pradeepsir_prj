from django.shortcuts import render, redirect
from dj_app.models import User, admine, Group
from .form import Userform, Groupform


def home(request):
    return render(request, 'home.html')


def create_user(request):
    edit_form = Userform()
    fm = Userform()
    if request.method == "POST":
        print("yoooooo")
        fm = Userform(request.POST)
        if fm.is_valid():
            fm.save()
    return render(request, 'create_user.html', {'form': edit_form})


def create_group(request):
    grup = Groupform()
    if request.method == "POST":
        fm = Groupform(request.POST)
        if fm.is_valid():
            fm.save()
    return render(request, 'create_group.html', {'form': grup})


def user(request):  # this admin may cause error in future
    user_data = User.objects.all()
    return render(request, 'user.html', {"aa": user_data})


def group(request):  # this admin may cause error in future
    group_data = Group.objects.all()
    return render(request, 'group.html', {"group": group_data})


def edit(request, id):
    get_user = User.objects.get(pk=id)
    edit_form = Userform(instance=get_user)
    if request.method == "POST":
        edit_form = Userform(request.POST, instance=get_user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('user')

    return render(request, 'edit_user.html', {'form': edit_form})
