from django.db import models, migrations
# Create your models here.

class Sign(models.Model):
    class Meta:
        db_table = 'Sign'
    s_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)



class User(models.Model):
    class Meta:
        db_table = 'User'
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    # birth_date = models.DateField(blank=True, null=True)
    user_type = models.CharField(max_length=255)
    organize_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    city_id = models.CharField(max_length=255)
    state_id = models.CharField(max_length=255)
    area_id = models.CharField(max_length=255)
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
    c_id = models.AutoField(primary_key=True)
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

# class Signup(models.Model):
#     class Meta:
#         db_table = 'Signup'
#     s_id = models.AutoField(primary_key=True)
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=255)

class Feedback(models.Model):
    class Meta:
        db_table = 'Feedback'
    f_id = models.AutoField(primary_key=True)
    subject= models.CharField(max_length=50)
    u_name = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    class Meta:
        db_table = 'Contact'
    c_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=255)
    comment = models.CharField(max_length=250)

# class Order(models.Model):
#     class Meta:
#         db_table = 'Order'
#     o_id = models.AutoField(primary_key=True)
#     u_id = models.IntegerField()
#     p_id = models.IntegerField()
#     quantity = models.IntegerField()
#     total_price = models.IntegerField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)

# class Purchases(models.Model):
#     class Meta:
#         db_table = 'Purchases'
#     # p_id = models.IntegerField(primary_key=True) # for postsql
#     p_id = models.AutoField(primary_key=True)
#     u_id = models.IntegerField()
#     p_id = models.IntegerField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)