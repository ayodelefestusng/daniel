# Generated by Django 5.0.7 on 2024-08-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0004_promocode_status_alter_promocode_gift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='code',
            field=models.CharField(max_length=11),
        ),
    ]
