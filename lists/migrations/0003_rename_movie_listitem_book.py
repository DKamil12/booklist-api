# Generated by Django 4.2 on 2024-08-23 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_alter_list_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='movie',
            new_name='book',
        ),
    ]
