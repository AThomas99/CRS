import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CreateStudentForm
from .models import *
from .decorators import admin_only, allowed_users, unauthenticated_user
    

@unauthenticated_user
def registerPage(request):
    # If user is logged in he/she should never access the register page through URL
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateStudentForm()

    if request.method == 'POST':    
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['first_name'] + request.POST['last_name']
            csee = request.POST['csee']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(first_name=first_name, last_name= last_name).exists():
                    messages.error(request, 'Password does not match')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Password does not match')
                else:
                    user = User.objects.create_user(
                        username = username,
                        first_name= first_name, 
                        last_name=last_name,
                        email=email,
                        password=password1
                    )
                    user.save()

                    group = Group.objects.get(name='student')
                    user.groups.add(group)

                    Student.objects.create(
                        user = user,
                        first_name = first_name,    
                        email = email,

                        csee = csee,
                    )
                    print('user creates successfully')


                messages.success(request, 'Account was created for ' + first_name)
                return redirect('login')

            else: 
                messages.error(request, 'Password does not match')
                return redirect('login')

    context = {}
    return render(request, 'core/auth/register.html', context)

@unauthenticated_user
def loginPage(request):
    # If user is logged in he/she should never access the login page through URL
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        email = request.POST.get('email') # update - make all username entered be lowercase
        password = request.POST.get('password')
        username = User.objects.get(email=email.lower()).username
        # print(username)
        # print(username + " " + password)
        # check if the user exists, if dont output a flash message
        try:
            user = User.objects.get(email=email)
            print(user)
        except:
            messages.error(request, 'User does not exist') # use flash error message

        # Get user object and authenticate based on username and password
        user = authenticate(request, username=username, password=password)

        if user is not None: # check if there is user or no user
            login(request, user) # Login the user and add the session into the db and browser
            return redirect('studentPage')

        else:
            messages.error(request, 'Username or password does not exist') # use flash error message
            print(user)
    context = {}
    return render(request, 'core/auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('studentPage')

@login_required(login_url='login')
@admin_only
def dashboard(request):
    return render(request, 'core/dashboard.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentPage(request):
    # orders = request.user.customer.order_set.all()

    # # These are statistical numbers for status.html
    # total_orders = orders.count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()

    context = {
        # 'orders': orders,
        # 'total_orders': total_orders,
        # 'delivered': delivered,
        # 'pending': pending,
    }
    return render(request, 'core/starter.html', context)



def recommendations(request):
    return render(request, 'core/recommendations.html')