# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import json

from django.views.decorators.csrf import csrf_exempt
from django import template

from .models import TeamMember, Project, Requirement
from .serializer import TeamMemberSerializer, ProjectSerializer, RequirementSerializer

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/list-members/")
@csrf_exempt #eximo autentificacion
def list_members(request):

    team_members = TeamMember.objects.all() 
    serializer = TeamMemberSerializer(team_members, many=True)

    return  JsonResponse(serializer.data, safe=False)

#@login_required(login_url="/list-projects/")
@csrf_exempt #eximo autentificacion
def list_projects(request):

    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return  JsonResponse(serializer.data, safe=False)

@csrf_exempt #eximo autentificacion
def GetRequirement(request):
    data = JSONParser().parse(request)
    requirements = Requirement.objects.get(pk=data["requirementId"])
    serializer = RequirementSerializer(requirements, many=False)

    return  JsonResponse(serializer.data, safe=False)

@csrf_exempt #eximo autentificacion
def GetRequirements(request):
    requirements = Requirement.objects.all()
    serializer = RequirementSerializer(requirements, many=True)

    return  JsonResponse(serializer.data, safe=False)

@csrf_exempt #eximo autentificacion
def SaveRequirement(request):
    data = JSONParser().parse(request)
    data = data["requirement"]
    print("DATA del front******:",data)
    requirementId = data['RequirementId']
    projectId = data['ProjectId']
    title = data['Title']
    description = data['Description']
    especificationLink = data['EspecificationLink']
    creation = data['Creation']
    edition = data['Edition']
    plannedEffort = data['PlannedEffort']
    realEffort = data['RealEffort']

    req = Requirement.objects.get(RequirementId=requirementId, ProjectId=projectId) #DavREQ01 / BancREQ01

    req.Title = title
    req.Description = description
    req.EspecificationLink = especificationLink
    req.Creation = creation
    req.Edition = edition
    req.PlannedEffort = plannedEffort
    req.RealEffort = realEffort

    req.save()    

    dataReturn = json.dumps(str("True"))
    return  JsonResponse(dataReturn, safe=False)   

@login_required(login_url="/switch-member/")
def switch_active_member(request,doc):

    member = TeamMember.objects.filter(Document=doc)
    member.update(Active=not('Active')) 
    return list_members(request)
    
@login_required(login_url="/update-member/")
def update_member(request, doc, names, mail, proxy_factor, av_week_hours, active):

    member = TeamMember.objects.filter(Document=doc)
    member.update(Document=doc, Names=names, Mail=mail, ProxyFactor=proxy_factor, AvailableWeekHours=av_week_hours, Active=not('Active')) 
    return list_members(request)

@login_required(login_url="/create-member/")
def create_member(request, doc, names, mail, proxy_factor, av_week_hours, active):

    TeamMember.objects.create(Document=doc, Names=names, Mail=mail, ProxyFactor=proxy_factor, AvailableWeekHours=av_week_hours, Active=not('Active')) 
    return list_members(request)


""" @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
 """