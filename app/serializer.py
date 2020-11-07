from rest_framework import serializers
from django.db import models
from .models import TeamMember
from .models import Project


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('Document', 'Names','ProxyFactor','AvailableWeekHours','Active','Mail')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('ProjectId', 'Title','Description','StartDate','EndDate','Active')        