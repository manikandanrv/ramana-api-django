# Generated by Django 4.0.2 on 2022-02-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0009_alter_request_likely_arrival_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='likely_arrival',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='likely_departure',
            field=models.DateField(),
        ),
    ]