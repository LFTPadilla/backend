from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)

admin.site.register(Requirement)
admin.site.register(Iteration)
admin.site.register(IterationTask)
admin.site.register(IterationTaskHistorial)

admin.site.register(TaskProxy)
admin.site.register(PlanningEntry)
admin.site.register(PlanningPeriod)
admin.site.register(TeamMember)
