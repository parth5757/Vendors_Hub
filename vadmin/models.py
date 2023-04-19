from django.db import models, migrations

# class Migration(migrations.Migration):
#     dependencies = []
#     operations = [
#         migrations.CreateModel(
#             name='PriceHistory',
#             fields=[
#                 ('id', models.AutoField(
#                     verbose_name='ID',
#                     serialize=False,
#                     primary_key=True,
#                     auto_created=True)),
#                 ('date', models.DateTimeField(auto_now_add=True)),
#                 ('price', models.DecimalField(decimal_places=2, max_digits=5)),
#                 ('volume', models.PositiveIntegerField()),
#                 ('total_btc', models.PositiveIntegerField()),
#             ],
#             options={
#             },
#             bases=(models.Model,),
#         ),
#     ]
# # from django.contrib.auth.models import User


# Create your models here.


class User(models.Model):
    class Meta:
        db_table = 'User'
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    user_phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    user_type = models.CharField(max_length=255)
    organize_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    city_id = models.IntegerField()
    state_id = models.IntegerField()
    area_id = models.IntegerField()
    gst_no = models.CharField(max_length=20)
    id_proof = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=255)

#     # def __str__(self):
#     #     return self.name

class Category(models.Model):
    class Meta:
        db_table = 'Category'
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    class Meta:
        db_table = 'Product'
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)    
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    discount = models.CharField(max_length=50)

class Signup(models.Model):
    class Meta:
        db_table = 'Signup'
    u_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

class Feedback(models.Model):
    class Meta:
        db_table = 'Feedback'
    f_id = models.AutoField(primary_key=True)
    subject= models.CharField(max_length=50)
    u_name = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


# class Contact(models.Model):
#     class Meta:
#         db_table = 'Contact'
#     c_id = models.AutoField(primary_key=True)
#     u_name = models.CharField(max_length=50)
#     u_email = models.EmailField(max_length=255)
#     comment = models.CharField(max_length=250)