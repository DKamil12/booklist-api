# Generated by Django 4.2 on 2024-08-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_rename_listfollowers_listfollower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='likes',
        ),
    ]
