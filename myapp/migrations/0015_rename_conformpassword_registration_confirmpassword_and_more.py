# Generated by Django 4.2.15 on 2024-09-02 05:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_registration_delete_mahesh_delete_student_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='ConformPassword',
            new_name='ConfirmPassword',
        ),
        migrations.AlterField(
            model_name='registration',
            name='Email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
