# Generated by Django 5.0.7 on 2024-08-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0008_alter_promocode_gift'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateGift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=11)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
    ]
