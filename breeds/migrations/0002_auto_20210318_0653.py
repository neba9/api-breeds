# Generated by Django 3.1.7 on 2021-03-18 06:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('breeds', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='breed',
            new_name='Breeds',
        ),
    ]