# Generated by Django 3.2.5 on 2023-04-23 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0022_rename_c_id_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='id',
            new_name='key',
        ),
    ]
