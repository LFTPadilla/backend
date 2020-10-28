# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.contrib.auth.models import User

#router = routers.DefaultRouter()
#router.register(r'', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
    path("auth/", include("authentication.urls")),
    path("app/", include("app.urls")),
    
]

"""


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', include(router.urls)),
    path("apigateway/", include("authentication.urls")),  # add this
    path("app/", include("app.urls"))  # add this
]
"""