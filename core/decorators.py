from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('studentPage')
            else:
                return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            print(allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Not allowed here..')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            print(group)
        if group == 'student':
            return redirect('studentPage')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
            
    return wrapper_func