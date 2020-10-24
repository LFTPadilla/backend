from django.db import models

# Create your models here.


class Project(models.Model):

    ProjectId = models.CharField(primary_key=True, max_length=50)

    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Active = models.BooleanField()

    def __str__(self):
        return self.Title
    #   return "{}|{}".format(self.ProjectId,self.Title)


class Requirement(models.Model):

    RequirementId = models.CharField(max_length=50, blank=False)
    ProjectId = models.ForeignKey(
        Project, on_delete=models.DO_NOTHING, blank=False)

    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    EspecificationLink = models.CharField(max_length=100)
    Creation = models.CharField(max_length=50)
    Edition = models.CharField(max_length=50)
    PlannedEffort = models.DecimalField(max_digits=3, decimal_places=1)
    RealEffort = models.DecimalField(max_digits=3, decimal_places=1)
    # State=
    # IterationTaskCode = models.OneToOneField('IterationTask', on_delete=models.DO_NOTHING)
    # IterationCode = models.ForeignKey('Iteration', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('RequirementId', 'ProjectId')

    def __str__(self):
        return "{}|{}".format(self.RequirementId, self.ProjectId.Title)

'''

class Iteration(models.Model):
 
   IterationCode = models.CharField(primary_key=True, max_length=50)
   ProjectId = models.ForeignKey('Project',on_delete=models.DO_NOTHING)
 
   Title =  models.CharField(max_length=50)
   StartDate = models.DateTimeField()
   PlannedEndDate = models.DateTimeField()
   RealEndDate = models.DateTimeField()
   PlannedEffort = models.DecimalField(max_digits=3,decimal_places=1)
   RealEffort = models.DecimalField(max_digits=3,decimal_places=1)
   Progress = models.DecimalField(max_digits=3,decimal_places=1)
  
   class Meta:
       unique_together = ('IterationCode','ProjectId')
 
   def __str__(self):
       return "{}|{}".format(self.IterationCode,self.Title)
 
class IterationTask(models.Model):
  
   IterationTaskCode = models.CharField(primary_key=True, max_length=50)
   IterationCode = models.ForeignKey('Iteration', on_delete=models.DO_NOTHING)
   ProjectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
 
   Title =  models.CharField(max_length=50)
   # TaskType =
   PlannedEffort = models.DecimalField(max_digits=3,decimal_places=1)
   RealEffort = models.DecimalField(max_digits=3,decimal_places=1)
   PlannedHours = models.DecimalField(max_digits=3,decimal_places=1)
   RealHours = models.DecimalField(max_digits=3,decimal_places=1)
   # State =
   Creation =  models.CharField(max_length=50)
   Edition =  models.CharField(max_length=50)
 
   class Meta:
       unique_together = ('IterationTaskCode','IterationCode','ProjectId')   
  
   def __str__(self):
       return "{}|{}".format(self.IterationTaskCode,self.Title)
 
 
class IterationTaskHistorial(models.Model):
  
   IterationTaskCode = models.ForeignKey('IterationTask', on_delete=models.DO_NOTHING)
   IterationCode = models.ForeignKey('Iteration', on_delete=models.DO_NOTHING)
   ProjectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
 
   Date = models.DateTimeField()
   Annotation =  models.CharField(max_length=250)
   # State=
  
   class Meta:
       unique_together = ('IterationTaskCode','IterationCode','ProjectId')   
 
   def __str__(self):
       return "{}".format(self.Date)
 
class TaskProxy(models.Model):
  
   IterationTaskCode = models.OneToOneField('IterationTask',on_delete=models.DO_NOTHING, )
   IterationCode = models.ForeignKey('Iteration', on_delete=models.DO_NOTHING)
   ProjectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
  
 
   Title =  models.CharField(max_length=50)
   Type =  models.CharField(max_length=50)
   EffortAvg = models.DecimalField(max_digits=3,decimal_places=1)
  
 
   class Meta:
       unique_together = ('IterationTaskCode','IterationCode','ProjectId')   
 
   def __str__(self):
       return "{}".format(self.Title)
 
class PlanningEntry(models.Model):
  
   PlanningEntryId = models.IntegerField(primary_key=True)
 
   Creation = models.CharField(max_length=50)
   Edition = models.CharField(max_length=50)
   PlannedHours = models.DecimalField(max_digits=3,decimal_places=1)
   RealHours = models.DecimalField(max_digits=3,decimal_places=1)
   PlannedEffort= models.DecimalField(max_digits=3,decimal_places=1)
   RealEffort = models.DecimalField(max_digits=3,decimal_places=1)
   # State =
   Anotation =  models.CharField(max_length=250)
   Document = models.ForeignKey('TeamMember',on_delete=models.DO_NOTHING)
   IterationTaskCode = models.ForeignKey('IterationTask', on_delete=models.DO_NOTHING)
   IterationCode = models.ForeignKey('Iteration', on_delete=models.DO_NOTHING)
   ProjectId = models.ForeignKey('Project',on_delete=models.DO_NOTHING)
 
 
   def __str__(self):
       return "PlanningEntry:{}".format(self.PlanningEntryId)
 
class PlanningPeriod(models.Model):
  
   PeriodId = models.CharField(primary_key=True, max_length=50)
   PlanningEntryId = models.OneToOneField('PlanningEntry',on_delete=models.DO_NOTHING)
 
   PeriodTitle = models.CharField(max_length=50)
   StartDate = models.DateTimeField()
   EndDate = models.DateTimeField()
   AvailableHours = models.IntegerField()
   PlannedEffort= models.DecimalField(max_digits=3,decimal_places=1)
   PlannedHours = models.DecimalField(max_digits=3,decimal_places=1)
   RealHours = models.DecimalField(max_digits=3,decimal_places=1)
   RealEffort = models.DecimalField(max_digits=3,decimal_places=1)
 
   # State =
   Anotation =  models.CharField(max_length=250)
 
   def __str__(self):
       return "{}|{}".format(self.PeriodId,self.PeriodTitle)
    
 
class TeamMember(models.Model):
  
   Document = models.CharField(primary_key=True, max_length=50)
 
   Names =  models.CharField(max_length=100)
   Mail =  models.CharField(max_length=100)
 
   ProxyFactor = models.DecimalField(max_digits=3,decimal_places=1)
   AvailableWeekHours = models.DecimalField(max_digits=3,decimal_places=1)
   Active = models.BooleanField()
  
   def __str__(self):
       return "{}|{}|{}".format(self.Document,self.Names,self.Active)
'''
