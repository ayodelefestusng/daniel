# Generated by Django 5.0.7 on 2024-08-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0016_alter_winning_code_items_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winning_code',
            name='items_name',
            field=models.CharField(max_length=11),
        ),
    ]
