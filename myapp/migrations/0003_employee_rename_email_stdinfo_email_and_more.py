# Generated by Django 4.2.15 on 2024-08-21 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_stdinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='stdinfo',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='stdinfo',
            old_name='password',
            new_name='Password',
        ),
    ]
