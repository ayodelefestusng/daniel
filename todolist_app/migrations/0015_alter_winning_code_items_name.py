# Generated by Django 5.0.7 on 2024-08-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0014_rename_qunatity_produced_winning_code_wcode_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winning_code',
            name='items_name',
            field=models.CharField(max_length=11),
        ),
    ]
