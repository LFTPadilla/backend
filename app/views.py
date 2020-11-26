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

from .models import TeamMember, Project, Requirement, Iteration, IterationTask, PlanningEntry
from .serializer import TeamMemberSerializer, ProjectSerializer, RequirementSerializer, IterationSerializer, TaskSerializer, PlanningEntrySerializer

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
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/list-members/")
@csrf_exempt  # eximo autentificacion
def list_members(request):

    team_members = TeamMember.objects.all()
    serializer = TeamMemberSerializer(team_members, many=True)

    return JsonResponse(serializer.data, safe=False)

# @login_required(login_url="/list-projects/")


@csrf_exempt  # eximo autentificacion
def GetProjects(request):

    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def SaveProject(request):
    data = JSONParser().parse(request)
    print("Data: ", data)
    data = data["project"]

    # Hay que ponerlo en el form o la otra es ponerla autoincr
    projectId = data["ProjectId"]
    title = data["Title"]
    description = data["Description"]
    startDate = data["StartDate"]
    endDate = data["EndDate"]
    active = str(data["Active"])
    print("AYYYYYYYYYYYYYYYYY", active)

    if active == "true":
        active = True
    else:
        active = False

    proy = Project(ProjectId=projectId, Title=title, Description=description, StartDate=startDate, EndDate=endDate,
                   Active=active)

    proy.save()

    dataReturn = json.dumps(str("True"))
    return JsonResponse(dataReturn, safe=False)


@csrf_exempt  # eximo autentificacion
def GetRequirement(request):
    data = JSONParser().parse(request)
    requirements = Requirement.objects.get(pk=data["requirementId"])
    serializer = RequirementSerializer(requirements, many=False)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt  # eximo autentificacion
def GetRequirements(request):
    # Obtener la info enviada del frontend
    data = JSONParser().parse(request)
    print("DATA del front******:", data)
    projectId = data["projectId"]
    # Buscar el proy con el id seleccionado (Todo el obj)
    project = Project.objects.get(ProjectId=projectId)
    # Filtrar para obtener los reqs con ese proy asociado
    requirements = Requirement.objects.filter(ProjectId=project)

    serializer = RequirementSerializer(requirements, many=True)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt  # eximo autentificacion
def SaveRequirement(request):
    data = JSONParser().parse(request)
    data = data["requirement"]
    print("DATA del front******:", data)
    requirementId = data['RequirementId']
    projectId = data['ProjectId']
    title = data['Title']
    description = data['Description']
    especificationLink = data['EspecificationLink']
    creation = data['Creation']
    edition = data['Edition']
    plannedEffort = data['PlannedEffort']
    realEffort = data['RealEffort']

    req = Requirement.objects.get(
        RequirementId=requirementId, ProjectId=projectId)  # DavREQ01 / BancREQ01

    req.Title = title
    req.Description = description
    req.EspecificationLink = especificationLink
    req.Creation = creation
    req.Edition = edition
    req.PlannedEffort = plannedEffort
    req.RealEffort = realEffort

    req.save()

    dataReturn = json.dumps(str("True"))
    return JsonResponse(dataReturn, safe=False)


@login_required(login_url="/switch-member/")
def switch_active_member(request, doc):

    member = TeamMember.objects.filter(Document=doc)
    member.update(Active=not('Active'))
    return list_members(request)


@login_required(login_url="/update-member/")
def update_member(request, doc, names, mail, proxy_factor, av_week_hours, active):

    member = TeamMember.objects.filter(Document=doc)
    member.update(Document=doc, Names=names, Mail=mail, ProxyFactor=proxy_factor,
                  AvailableWeekHours=av_week_hours, Active=not('Active'))
    return list_members(request)


@login_required(login_url="/create-member/")
def create_member(request, doc, names, mail, proxy_factor, av_week_hours, active):

    TeamMember.objects.create(Document=doc, Names=names, Mail=mail, ProxyFactor=proxy_factor,
                              AvailableWeekHours=av_week_hours, Active=not('Active'))
    return list_members(request)


@csrf_exempt
def GetIterations(request):
    data = JSONParser().parse(request)
    # print("AAAAAAAAAAH",data)
    projectId = data["projectId"]
    # print("Proyecto Seleccionado",projectId)
    iterations = Iteration.objects.filter(ProjectId=projectId)
    serializer = IterationSerializer(iterations, many=True)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def SaveIteration(request):
    data = JSONParser().parse(request)
    print("Data: ", data)
    data = data["iteration"]

    # Hay que ponerlo en el form o la otra es ponerla autoincr
    iterationCode = data["IterationCode"]
    projectId = data["ProjectId"]
    title = data["Title"]
    startDate = data["StartDate"]
    plannedEndDate = data["PlannedEndDate"]
    # realEndDate = data["RealEndDate"]
    plannedEffort = data["PlannedEffort"]
    # realEffort = data["RealEffort"]
    # progress = data["Progress"]

    project = Project.objects.get(pk=projectId)

    existIter = Iteration.objects.get( ProjectId=project, IterationCode=iterationCode) 
    if(existIter):
        existIter.Title = title
        existIter.StartDate = startDate
        existIter.PlannedEndDate = plannedEndDate
        existIter.PlannedEffort = plannedEffort        
        existIter.save()
    else:
        it = Iteration(IterationCode=iterationCode, ProjectId=project, Title=title, StartDate=startDate, PlannedEndDate=plannedEndDate,
                   PlannedEffort=plannedEffort)
        it.save()

    dataReturn = json.dumps(str("True"))
    return JsonResponse(dataReturn, safe=False)


@csrf_exempt
def GetTasks(request):
    data = JSONParser().parse(request)
    print("AAAAAAAAAAH", data)
    projectId = data["projectId"]
    iterationCode = data["iterationCode"]

    project = Project.objects.get(pk=projectId)
    iteration = Iteration.objects.get(
        IterationCode=iterationCode, ProjectId=projectId)

    tasks = IterationTask.objects.filter(
        ProjectId=project, IterationCode=iteration)

    serializer = TaskSerializer(tasks, many=True)
    tasksSerialized = serializer.data
    for i in tasksSerialized:
        #print('TAREA',i['ProjectId'],i['IterationCode'],i['IterationTaskCode'])
        
        task = IterationTask.objects.get(ProjectId=project, IterationCode=iteration,IterationTaskCode=i['IterationTaskCode'] )
        plan = PlanningEntry.objects.filter(ProjectId=project, IterationCode=iteration,IterationTaskCode=task)
        serializerPlan = PlanningEntrySerializer(plan, many=True).data
        i['Planning'] = serializerPlan
    

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def SaveTask(request):
    data = JSONParser().parse(request)
    print("Data: ", data)
    data = data["task"]

    taskCode = data["IterationTaskCode"]
    taskTitle = data["Title"]
    taskType = data["TaskType"]
    iterationCode = data["IterationCode"]
    projectId = data["ProjectId"]
    requirementId = data["RequirementId"]
    plannedEffort = data["PlannedEffort"]
    realEffort = data["RealEffort"]
    plannedHours = data["PlannedHours"]
    realHours = data["RealHours"]
    state = data["State"]
    creation = data["Creation"]
    edition = data["Edition"]

    project = Project.objects.get(pk=projectId)
    iteration = Iteration.objects.get(
        IterationCode=iterationCode, ProjectId=projectId)
    req = Requirement.objects.get(
        RequirementId=requirementId, ProjectId=projectId)

    task = IterationTask(IterationTaskCode=taskCode, IterationCode=iteration, ProjectId=project,
                         RequirementId=req, Title=taskTitle, TaskType=taskType, PlannedEffort=plannedEffort,
                         RealEffort=realEffort, PlannedHours=plannedHours, RealHours=realHours, State=state)

    task.save()

    dataReturn = json.dumps(str("True"))
    return JsonResponse(dataReturn, safe=False)


@csrf_exempt
def GetPlanningEntries(request):
    data = JSONParser().parse(request)
    print("PPPPPPPPPPPPPPPPPPPPPP", data)
    projectId = data["projectId"]
    iterationCode = data["iterationCode"]
    iterationTaskCode = data["iterationTaskCode"]

    project = Project.objects.get(pk=projectId)
    print("Proy",project)
    iteration = Iteration.objects.get(
        IterationCode=iterationCode, ProjectId=project)
    print("Itera",iteration)

    task = IterationTask.objects.filter(
        ProjectId=project, IterationCode=iteration, IterationTaskCode=iterationTaskCode)
    print("Tarea",task)

    pEntries = PlanningEntry.objects.filter(
        ProjectId=project, IterationCode=iteration, IterationTaskCode=task)
    print("Planning Entries",pEntries)

    serializer = PlanningEntrySerializer(pEntries, many=True)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def SavePlanningEntry(request):
    data = JSONParser().parse(request)
    print("Data: ", data)
    data = data["planningEntry"]

    iterationCode = data["IterationCode"]
    projectId = data["ProjectId"]
    iterationTaskCode = data["IterationTaskCode"]
    creation = data["Creation"]
    edition = data["Edition"]
    plannedHours = data["PlannedHours"]
    realHours = data["RealHours"]
    plannedEffort = data["PlannedEffort"]
    realEffort = data["RealEffort"]
    state = data["State"]
    annotation = data["Annotation"]
    startDate = data["StartDate"]
    endDate = data["EndDate"]
    document = data["Document"]

    project = Project.objects.get(pk=projectId)
    iteration = Iteration.objects.get(
        IterationCode=iterationCode, ProjectId=projectId)
    print("BUSSSSCANDOOOOOOOOO la tarea con iteracion:",
          iteration, "y proyecto", project)

    task = IterationTask.objects.get(
        IterationTaskCode=iterationTaskCode, IterationCode=iteration, ProjectId=projectId)

    if document == "":
        member = None
    else:
        member = TeamMember.objects.get(Document=document)

    # Buscar al member por el document

    planningEntry = PlanningEntry(IterationTaskCode=task, IterationCode=iteration, ProjectId=project,
                                  Creation=creation, Edition=edition, PlannedHours=plannedHours,
                                  RealHours=realHours, PlannedEffort=plannedEffort,
                                  RealEffort=realEffort, State=state, Anotation=annotation, StartDate=startDate,
                                  EndDate=endDate, Document=member)

    planningEntry.save()

    serializerPlan = PlanningEntrySerializer(planningEntry,many=False)
    idPlan = serializerPlan.data['PlanningEntryId']   
     
    
    return JsonResponse({'PlaningEntryId':idPlan}, safe=False)

@csrf_exempt
def SaveNewStatePlanningEntry(request):
    data = JSONParser().parse(request)
    print("Data: ", data)
    
    pEntryId = data["pEntryId"]
    taskCode = data["taskcode"]
    iterationCode = data["iterationCode"]
    projectId = data["projectId"]
    state = data["state"]

    project = Project.objects.get(pk=projectId)
    iteration = Iteration.objects.get(
        IterationCode=iterationCode, ProjectId=projectId)
    
    task = IterationTask.objects.get(IterationTaskCode=taskCode, IterationCode=iteration, ProjectId=project)

    planningEntry = PlanningEntry.objects.get(pk=pEntryId)

    task.State = state
    planningEntry.State = state

    task.save()
    planningEntry.save()

    dataReturn = json.dumps(str("True"))
    return JsonResponse(dataReturn, safe=False)


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
