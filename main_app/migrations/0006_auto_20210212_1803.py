# Generated by Django 3.0.6 on 2021-02-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210212_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.BigIntegerField(default=916370926031),
        ),
    ]