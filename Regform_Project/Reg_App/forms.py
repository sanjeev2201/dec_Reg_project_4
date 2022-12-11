from django import forms
from .models import Customer

# Create django form
class CustomerForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    conf_pass=forms.CharField(widget=forms.PasswordInput())
    class Meta:
            model = Customer
            fields = ("Customer_Id","Customer_name","email_Id","password","conf_pass","Contact_no")
    
    


