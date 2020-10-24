from django.contrib import admin
from django.urls import path
from djangoapp.api import views
from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]