# Generated by Django 3.2.7 on 2021-09-25 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_project_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='author',
            new_name='user',
        ),
    ]