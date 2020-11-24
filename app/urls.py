# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('list-members/', views.list_members, name='list-members'),
    path('GetRequirements/', views.GetRequirements, name='GetRequirements'),
    path('GetRequirement/', views.GetRequirement, name='GetRequirement'),
    path('SaveRequirement/', views.SaveRequirement, name='SaveRequirement'),
    path('switch-member/', views.switch_active_member, name='switch-member'),
    path('GetProjects/', views.GetProjects, name='GetProjects'),
    path('SaveProject/', views.SaveProject, name='SaveProject'),
    path('GetIterations/', views.GetIterations, name='GetIterations'),
    path('SaveIteration/', views.SaveIteration, name='SaveIteration'),
    path('GetTasks/', views.GetTasks, name='GetTasks'),
    path('SaveTask/', views.SaveTask, name='SaveTask'),
    path('SavePlanningEntry/', views.SavePlanningEntry, name='SavePlanningEntry')

]
