# Generated by Django 5.1.1 on 2024-10-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hosapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointmentshedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('time', models.TimeField()),
            ],
        ),
    ]
