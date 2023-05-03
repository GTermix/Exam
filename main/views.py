from django.shortcuts import render, redirect
from .forms import *


def index(req):
    data = Registration.objects.all()
    return render(req, 'index.html', {"data": data})


def students(req):
    form = StudentsForm()
    if req.method == "POST":
        form = StudentsForm(req.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    return render(req, 'student.html', {'form': form})


def registration(req):
    form = RegistrationForm()
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    return render(req, 'registration.html', {'form': form})
