# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase
from .models import Project, Iteration,Requirement, IterationTask, TaskProxy
import datetime

from django.utils import timezone


class ProjectTest(TestCase):
    """ Test module for Project model """

    def setUp(self):
        proj = Project.objects.create(ProjectId='Proj', Title='Proyecto prueba', Description='pruebas', StartDate=timezone.now(), EndDate=timezone.now(),Active=True)
        
        itera = Iteration.objects.create(IterationCode="Iter1",ProjectId=proj,Title="Iteracion prueba",StartDate=timezone.now(), PlannedEndDate=timezone.now(),PlannedEffort=2.5)
        
        req = Requirement.objects.create(RequirementId="req1",ProjectId=proj,Title="Requerimiento prueba",Description="Desarrollo",EspecificationLink="", State="Planned",Creation="",Edition="",PlannedEffort=2.5,RealEffort=3)

        task = IterationTask.objects.create(IterationTaskCode="task1",IterationCode=itera,ProjectId=proj,RequirementId=req,Title="Tarea prueba",TaskType="Desarrollo",PlannedHours=20, State="Planned",Creation="",Edition="",PlannedEffort=2.5)
        
        proxy = TaskProxy.objects.create(IterationTaskCode=task,IterationCode=itera,ProjectId=proj,Title="Proxy prueba",Type="Desarrollador",EffortAvg=20)


    def test_project(self):
        proj = Project.objects.get(ProjectId='Proj')
        self.assertEqual(proj.get_main(), "Proj: Proyecto prueba")

    def test_iteration(self):
        itera = Iteration.objects.get(IterationCode="Iter1")
        self.assertEqual(itera.get_main(), "Iter1: Iteracion prueba")

    def test_requirement(self):
        req = Requirement.objects.get(RequirementId="req1")
        self.assertEqual(req.get_main(), "req1: Requerimiento prueba")

    def test_task(self):
        task = IterationTask.objects.get(IterationTaskCode='task1')
        self.assertEqual(task.get_main(), "task1: Tarea prueba")

    def test_TaskProxy(self):
        proxy = TaskProxy.objects.get(ProjectId='Proj')
        self.assertEqual(proxy.get_main(), "Desarrollador: Proxy prueba")
        
        
