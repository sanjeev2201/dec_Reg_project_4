from django import forms
from .models import Customer

# Create django form
class CustomerForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    conf_pass=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}))
    class Meta:
            model = Customer
            fields = ("Customer_Id","Customer_name","email_Id","password","conf_pass","Contact_no")


            widgets = {
            'Customer_Id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Id'}),
            'Customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer name'}),
            'email_Id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email Id'}),
            'Contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobile number'})
        }
    
    


