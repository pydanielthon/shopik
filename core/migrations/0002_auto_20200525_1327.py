# Generated by Django 2.2.10 on 2020-05-25 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='kategoria',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
