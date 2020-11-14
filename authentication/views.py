# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, SignUpForm

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .model.ServiceObject import ServiceObject,ServiceObjectEncoder
from rest_framework import routers,  viewsets #serializers,
from django.core import serializers
from rest_framework.parsers import JSONParser
import base64
import json
from django.views.decorators.csrf import csrf_protect

from app.models import TeamMember
from app.serializer import TeamMemberSerializer

@csrf_exempt 
def login_view(request):
    
    result = False
    userSerilized = None
    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data['login']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            member = TeamMember.objects.filter(user=user)
            serializer = TeamMemberSerializer(member, many=True)
            userSerilized = serializer.data[0]
            print(serializer.data[0])
            login(request, user)
            result = True
    
    return  JsonResponse({'Success':result, 'User':userSerilized}, safe=False)

    

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
