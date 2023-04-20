from django.contrib import admin
from .models import Signup, User, Category, Product, Feedback, Contact

class SignupAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'email', 'password')
admin.site.register(Signup, SignupAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_email', 'user_phone_number', 'birth_date', 'user_type', 'organize_name', 'city_id', 'state_id', 'area_id', 'gst_no', 'id_proof', 'created_date', 'created_by', 'modified_date', 'modified_by')
    search_fields = ('user_id', 'user_name', 'user_email', 'user_phone_number', 'organize_name', 'gst_no')
    list_filter = ('user_type', 'city_id', 'state_id', 'area_id')
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')

admin.site.register(User, UserAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description', 'created_date', 'modified_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'name', 'price', 'description', 'category', 'quantity', 'brand', 'stock', 'discount')

admin.site.register(Product, ProductAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('f_id', 'subject', 'u_name', 'message')

admin.site.register(Feedback, FeedbackAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'u_name', 'u_email', 'comment')

admin.site.register(Contact, ContactAdmin)