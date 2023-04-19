# Generated by Django 2.2.16 on 2023-04-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vadmin', '0012_remove_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
