# Generated by Django 4.0.2 on 2022-02-02 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devotee',
            name='linenos',
        ),
    ]
