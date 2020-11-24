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
    Member = None
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        username = data['login']
        password = data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            member = TeamMember.objects.filter(user=user)
            serializer = TeamMemberSerializer(member, many=True)
            Member = serializer.data[0]
            print(serializer.data[0])
            if(username=='roa'):
                Member['Permissions'] = ['planner-scrum']
            else:
                Member['Permissions'] = ['planner-member']
            login(request, user)
            result = True
    
    return  JsonResponse({'Success':result, 'User':{'Member':Member}}, safe=False)

    

@csrf_exempt 
def register_user(request):
    data = JSONParser().parse(request)
    print(data)
    username = data['login']
    document = data['document']
    email = data['email']
    password = data['password']
    
    msg = ''
    scc = None


    #VALIDACIONES
    try:
        userExist = User.objects.filter(username=username)
        print(userExist)
        if(userExist):
            raise ValueError('El username '+username+' ya se encuentra registrado.')
            
        emailExist = User.objects.filter(email=email)
        if(emailExist):
            raise ValueError('El email '+email+' ya se encuentra registrado.')

        member = TeamMember.objects.filter(Document=document)
        if(member):
            raise ValueError('El documento '+documento+' ya se encuentra registrado.')
            
    except ValueError as msg:
        return  JsonResponse({'Success':False, 'Message': msg.args[0], 'User':None}, safe=False)
    except Exception as err:
        print("ERRORR",err)
        return  JsonResponse({'Success':False, 'Message': "ServerError "+ err.args[0], 'User':None}, safe=False)

    try:
        user = User.objects.create(username=username,email=email)
        user.set_password(password)
        user.save()
        member = TeamMember.objects.create(user=user,Mail=email,ProxyFactor=0,AvailableWeekHours=40,Active=True,Names="",Document=document)
        serializer = TeamMemberSerializer(member, many=False)
        print(serializer.data)
        return  JsonResponse({'Success':True,'Message': '', 'User':serializer.data}, safe=False)
    except Exception as err:
        return  JsonResponse({'Success':False,'Message': "ServerError "+ err.args[0], 'User':None}, safe=False)
   
