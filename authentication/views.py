# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, SignUpForm
import base64
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .model.ServiceObject import ServiceObject,ServiceObjectEncoder
from rest_framework import routers, serializers, viewsets
from rest_framework.parsers import JSONParser
import json
from django.views.decorators.csrf import csrf_protect
from app.model.service_object import ServiceObject


@csrf_exempt 
def login_view(request):
    serviceObj = {
        "Success": False,
        "Messege": '',
        "Data":[]
    };
    print(serviceObj)
    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data['login']
        password = data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            log = login(request, user)
            serviceObj.Success = True
            print(log)
        else:
            msg = 'Invalid credentials'   

    dataReturn = json.dumps(str(serviceObj))

    print(dataReturn)
    print(json.loads(str(serviceObj.__dict__)))
    return  JsonResponse(dataReturn, safe=False)
    #return render(request, "accounts/login.html", {"form": form, "msg" : msg})

    

def register_user(request):

    msg     = None
    success = False
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
