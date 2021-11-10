from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager
import bcrypt

def index(request):
    request.session.flush()
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        errors=User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(rounds = 10)).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash,
        )
        request.session['user_id'] = new_user.id
        return redirect('/detales')
    return redirect('/')

def login_user(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/detales')
    return redirect('/')

def detales(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0]
    }
    return render(request, 'detales.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
    
    

