# Generated by Django 5.0.7 on 2024-08-05 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_alter_promocode_gift'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='Status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='gift',
            field=models.CharField(max_length=200),
        ),
    ]
