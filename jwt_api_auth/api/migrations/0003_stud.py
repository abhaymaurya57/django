# Generated by Django 5.2 on 2025-06-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cource'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
