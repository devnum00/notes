from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
@login_required(login_url="/login/")
def index(request):
    notes = Note.objects.filter(user=request.user).order_by('-date_created')
    context = {
        "notes": notes,
        'range': range(255),
    }
    return render(request, "base/index.html",context)
@login_required(login_url="/login/")
def add_note(request):
    if request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']
        user = request.user  
        new_note = Note(user=user,title=title,text=text)
        new_note.save()
        return redirect("/")
    return render(request, "base/add_note.html")
@login_required(login_url="/login/")
def update_note(request, pk):
    note = get_object_or_404(Note,pk=pk,  user=request.user)
    if request.method == "POST":
        note.title = request.POST['title']
        note.text = request.POST['text']
        note.save()
        return redirect("/")
    context = {
        "note":note,
    }
    return render(request, "base/update_note.html", context)
@login_required(login_url="/login/")
def delete_note(request, pk):
    note = get_object_or_404(Note,pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("/")

    context={
        "note":note,
    }
    return render(request, "base/delete_note.html",context)

@login_required(login_url="/login/")
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk,  user=request.user)
    context={
        "note":note
    }
    return render(request, "base/note_detail.html",context)



def register_user(request):
    if request.method=="POST":
        firstname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']
        if password_1 == password_2:
            new_user = User.objects.create_user(username=username,email=email, password=password_1, first_name=firstname)
            new_user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('/login/')
        else:
            messages.error(request, 'Passwords Does not match')

            return redirect('/register/')
    return render(request, "base/register.html")

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')
    return render(request, "base/login.html")

def logout_user(request):
    logout(request)
    return redirect('/login/')

def custom_404(request, exception):
    return render(request, '404.html', status=404)