# Generated by Django 4.2.15 on 2024-09-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_registration_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='std_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=30)),
                ('Number', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
