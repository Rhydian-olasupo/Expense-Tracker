# Generated by Django 4.2 on 2023-06-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]