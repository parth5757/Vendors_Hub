from django import forms
from .models import User, Product
    
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ['user_name', 'user_email', 'user_phone_number', 'password', 'confirm_password', 'organize_name', 'birth_date', 'city_id', 'state_id', 'area_id', 'gst_no', 'id_proof']
    
#     # def clean(self):
#     #     cleaned_data = super(UserForm, self).clean()
#     #     password = cleaned_data.get('password')
#     #     confirm_password = cleaned_data.get('confirm_password')
#     #     if password and confirm_password:
#     #         if password != confirm_password:
#     #             raise forms.ValidationError("Passwords do not match")
#     #     return cleaned_data


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'quantity', 'brand', 'stock', 'discount']
