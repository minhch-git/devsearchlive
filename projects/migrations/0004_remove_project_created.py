# Generated by Django 3.2.7 on 2021-09-13 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created',
        ),
    ]