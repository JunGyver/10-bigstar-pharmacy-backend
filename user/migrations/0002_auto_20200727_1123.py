# Generated by Django 3.0.8 on 2020-07-27 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mobile_number',
            new_name='contact',
        ),
    ]
