from rest_framework import serializers
from django.db import models
from .models import TeamMember, Requirement, Project, Iteration


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
        fields = ('IterationCode', 'Title', 'StartDate', 'PlannedEndDate', 
        'RealEndDate', 'PlannedEffort', 'RealEffort', 'Progress')        