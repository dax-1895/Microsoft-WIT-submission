# Generated by Django 3.0.6 on 2021-02-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.PositiveIntegerField(default=123456789),
        ),
    ]
