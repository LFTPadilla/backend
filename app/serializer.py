from rest_framework import serializers
from django.db import models
from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('Document', 'Names','ProxyFactor','AvailableWeekHours','Active','Mail')