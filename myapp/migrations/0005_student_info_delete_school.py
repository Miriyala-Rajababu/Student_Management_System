# Generated by Django 4.2.15 on 2024-08-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_school_delete_employee_delete_stdinfo_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Course', models.CharField(max_length=20)),
                ('Fee', models.IntegerField(max_length=20)),
                ('Date', models.DateField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='school',
        ),
    ]
