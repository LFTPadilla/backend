from django.contrib.auth.models import User, Group
from .models import Project
from rest_framework import viewsets
from rest_framework import permissions
from djangoapp.api.serializers import UserSerializer,ProjectSerializer
import requests

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-StartDate')
    serializer_class = ProjectSerializer
