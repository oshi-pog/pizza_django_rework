# Generated by Django 3.1.3 on 2020-11-26 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0002_auto_20201126_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='user',
        ),
    ]