# Generated by Django 4.2.15 on 2024-09-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_std_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='std_result',
            name='Hallticket',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]
