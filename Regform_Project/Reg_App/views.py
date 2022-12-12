from django.shortcuts import render,redirect,HttpResponse
from .forms import CustomerForm
from .models import Customer
#"Customer_Id","Customer_name","email_Id","password","conf_pass","Contact_no"
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import datetime
# Create your views here.
def registration(request):
    if request.method == 'POST':
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
                    messages.success(request, "customer added successful." )
                    return redirect('list_contact')
                else:
                    print('please enter ten digit mobile number')
                    messages.error(request,"please enter ten digit mobile number")
            else:
                print("password is not matching")
                messages.error(request,"password is not matching")
            
    else:
        fm=CustomerForm()
    return render(request,'Reg_App/reg.html',{'form':fm})

def list_contact(request):
    retrieve_data = Customer.objects.all()
    current_time=datetime.datetime.now()
    context = {'customers':retrieve_data,
    'current_time':current_time}
    return render(request,'Reg_App/list.html',context)

def customer_edit(request,pk):
    customer = Customer.objects.get(Customer_Id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('list_contact')

    context = {
        'customer': customer,
        'form': form,
    }
    return render(request, 'Reg_App/edit.html', context)

def customer_delete(request,pk):
    customer = Customer.objects.get(Customer_Id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('list_contact')

    context = {
        'customer': customer,
    }
    return render(request, 'Reg_App/delete.html', context)

#create user
def create_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('registration')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form=UserCreationForm()
    return render(request,'Reg_App/create_user.html',{'form':form})

#login request
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("registration")
			else:
				messages.error(request,"user already created")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"Reg_App/login.html",{"login_form":form})


#log out request
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")