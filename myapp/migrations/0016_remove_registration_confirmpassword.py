# Generated by Django 4.2.15 on 2024-09-02 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_conformpassword_registration_confirmpassword_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='ConfirmPassword',
        ),
    ]
