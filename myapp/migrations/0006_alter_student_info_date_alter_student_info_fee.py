# Generated by Django 4.2.15 on 2024-08-25 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_student_info_delete_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Fee',
            field=models.IntegerField(),
        ),
    ]