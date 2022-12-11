from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
#"Customer_Id","Customer_name","email_Id","password","conf_pass","Contact_no")
# Create your views here.
def registration(request):
    if request.method == 'POST':
        Customer.objects.all()
        fm = CustomerForm(request.POST)
        if fm.is_valid():
            cus_id = fm.cleaned_data['Customer_Id']
            cus_nm = fm.cleaned_data['Customer_name']
            em_id = fm.cleaned_data['email_Id']
            pas=fm.cleaned_data['password']
            confpas = fm.cleaned_data['conf_pass']
            contactno=fm.cleaned_data['Contact_no']
            if pas == confpas:
                if len(contactno)==10:
                    reg = Customer(Customer_Id=cus_id,Customer_name=cus_nm,email_Id=em_id,password=pas,conf_pass=confpas,Contact_no=contactno)
                    reg.save()
                    print("record has been save in database")
                else:
                    print('please enter ten digit mobile number')
            else:
                print("password is not matching")
            
    else:
        fm=CustomerForm()
    return render(request,'Reg_App/reg.html',{'form':fm})