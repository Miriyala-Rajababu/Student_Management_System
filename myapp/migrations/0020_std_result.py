# Generated by Django 4.2.15 on 2024-09-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_rename_std_reg_std_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='std_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Cource', models.CharField(max_length=30)),
                ('result', models.CharField(max_length=20)),
            ],
        ),
    ]