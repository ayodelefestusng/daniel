# Generated by Django 5.0.7 on 2024-08-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='code',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
