from django.shortcuts import render,redirect
from users.forms import UserRegistrationForm,DriverRegistraionForm,UserProfileCreationForm
# Create your views here.
from .models import Userprofile,Driverprofile



def signup(request):
    return render(request,'users/signup.html')

def register_driver(request):
    u_form = UserRegistrationForm()
    d_form = DriverRegistraionForm()
    up_form = UserProfileCreationForm()

    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        d_form = DriverRegistraionForm(request.POST)
        up_form = UserProfileCreationForm(request.POST)

        if u_form.is_valid():
            if d_form.is_valid():
                if up_form.is_valid():

                    user = u_form.save()
                    d_form.save()
                   
                    user_profile =  up_form.save(commit=False)
                    user_profile.user = user
                    user_profile.is_driver = True

                    user_profile.save()
                    return redirect('login')
    return render(request,'users/register_driver.html',{ 'u_form':u_form , 'd_form':d_form, 'up_form':up_form})

def register_passenger(request):
    u_form = UserRegistrationForm()
    up_form = UserProfileCreationForm()
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        up_form = UserProfileCreationForm(request.POST)
    if u_form.is_valid():
            
                if up_form.is_valid():

                    user = u_form.save()
                    user_profile =  up_form.save(commit=False)
                    user_profile.user = user
                    user_profile.save()
                    return redirect('login')

    return render(request,'users/register_passenger.html',{ 'u_form':u_form , 'up_form':up_form})


# def hh(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()

#     return
