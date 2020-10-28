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
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt #eximo autentificacion
def login_view(request):
    msg = None
    serviceObj = ServiceObject('Auth','','CreateSession')
    print('request ', request)
    
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        user = authenticate(username=data['login'], password=data['password'])
        print("USUARIO ",user)
        if user is not None:
            userSerializer = UserSerializer(user,many=False)
            serviceObj.User = userSerializer.data
            login(request, user)
            serviceObj.Success = True
        else:    
            serviceObj.Messege = 'Invalid credentials' 
        
    
    return JsonResponse(serviceObj.toJson(), safe=False)
    

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
