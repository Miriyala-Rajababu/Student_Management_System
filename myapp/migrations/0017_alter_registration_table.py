# Generated by Django 4.2.15 on 2024-09-02 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_registration_confirmpassword'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='registration',
            table='student_data',
        ),
    ]
