from django.db import models


class admine(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.first_name


class User(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    phone_no = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.first_name


class Group(models.Model):
    group_name = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    add_user = models.ManyToManyField(User)

    def __str__(self):
        return self.group_name
