# Generated by Django 4.0.2 on 2022-02-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0005_remove_room_house_keeping_instruction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guesthouse_name',
            field=models.CharField(blank=True, choices=[('K', 'Kurangu Thottam'), ('A1', 'A Rooms'), ('A', 'Dispensary'), ('AA', 'Achalam Guest House'), ('R', 'Post Office Rooms'), ('M', 'Mourvi Guest House')], default='K', max_length=70),
        ),
    ]
