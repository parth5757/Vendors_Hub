# Generated by Django 3.2.5 on 2023-05-01 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0032_sign'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Purchases',
        ),
    ]