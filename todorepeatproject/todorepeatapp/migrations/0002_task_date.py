# Generated by Django 3.2.12 on 2022-03-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todorepeatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-07-21'),
            preserve_default=False,
        ),
    ]
