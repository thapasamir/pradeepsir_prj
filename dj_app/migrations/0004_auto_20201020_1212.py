# Generated by Django 3.1.2 on 2020-10-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app', '0003_auto_20201020_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='add_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dj_app.user'),
        ),
    ]
