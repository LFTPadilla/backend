# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase
from .models import Project


class ProjectTest(TestCase):
    """ Test module for Project model """

    def setUp(self):
        Project.objects.create(
            ProjectId='Proj', Title='Proyectico', Description='pruebas', StartDate="2020-11-01", EndDate="2020-11-20",Active=True)

    def test_project(self):
        proj = Project.objects.get(ProjectId='Proj')
        print(proj.get_main())
        self.assertEqual(
            proj.get_main(), "Proj: Proyectico")
        
