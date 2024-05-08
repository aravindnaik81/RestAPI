# Generated by Django 4.2.7 on 2024-05-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactBook',
            fields=[
                ('Name', models.CharField(max_length=50)),
                ('Phone_Number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('SIM', models.CharField(max_length=20)),
            ],
        ),
    ]