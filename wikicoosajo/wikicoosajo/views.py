# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        if request.method == "GET":
            return render(request, "login.html")
        elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    next = "/"
                    if "next" in request.GET:
                        next = request.GET["next"]
                    if next == None or next == "":
                        next = "/"
                    return redirect(next)
                else:
                    return render(request, "login.html", {"mensaje": "Tu cuenta ha sido deshabilitada"})
            else:
                return render(request, "login.html", {"mensaje": "Usuario o contraseña incorrecta"})
@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")
