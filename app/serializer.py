from rest_framework import serializers
from django.db import models
from .models import TeamMember, Requirement, Project, Iteration, IterationTask, PlanningEntry


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('Document', 'Names','ProxyFactor','AvailableWeekHours','Active','Mail')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('ProjectId', 'Title','Description','StartDate','EndDate','Active')        

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement 
        fields = ('RequirementId', 'ProjectId', 'Title', 'Description', 'EspecificationLink', 
        'Creation', 'Edition', 'PlannedEffort', 'RealEffort')

class IterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iteration 
        fields = ('IterationCode', 'ProjectId', 'Title', 'StartDate', 'PlannedEndDate', 
        'RealEndDate', 'PlannedEffort', 'RealEffort', 'Progress')        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = IterationTask 
        fields = ('IterationTaskCode','IterationCode','ProjectId', 'RequirementId', 'Title', 'TaskType',
        'PlannedEffort', 'RealEffort', 'PlannedHours', 'RealHours', 'State', 'Creation', 'Edition')


class PlanningEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanningEntry 
        fields = ('PlanningEntryId','IterationTaskCode','IterationCode','ProjectId', 'StartDate', 'EndDate',
        'State', 'RealEffort', 'PlannedHours', 'RealHours', 'Creation', 'Edition')
