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

'''
    Pueden existir:
        ProyDavivienda_REQ01
        ProyBancolombi_REQ01
        La combinación de ambas debe ser única.
'''
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
    Pueden existir:
        ProyDavivienda_It01
        ProyBancolombi_It01
        La combinación de ambas debe ser única.
    Queda una llave (id) generada automáticamente como primaria e incremental.    
'''
class Iteration(models.Model):

    IterationCode = models.CharField(max_length=50, blank=False)
    ProjectId = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False)

    Title = models.CharField(max_length=50)
    StartDate = models.DateTimeField()
    PlannedEndDate = models.DateTimeField()
    RealEndDate = models.DateTimeField()
    PlannedEffort = models.DecimalField(max_digits=3, decimal_places=1)
    RealEffort = models.DecimalField(max_digits=3, decimal_places=1)
    Progress = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        unique_together = ('IterationCode', 'ProjectId')

    def __str__(self):
        return "{}|{}".format(self.ProjectId, self.IterationCode)


'''
    Pueden existir:
        ProyDavivienda_It01_T33
        ProyDavivienda_It01_T34
        ProyBancolombi_It01_T33
 '''
class IterationTask(models.Model):
    
    IterationTaskCode = models.CharField(max_length=50, blank=False)
    IterationCode = models.ForeignKey(Iteration, on_delete=models.DO_NOTHING, blank=False)
    ProjectId = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False ) #, editable=False)   
    Title = models.CharField(max_length=50, blank=False)
    # TaskType =
    PlannedEffort = models.DecimalField(max_digits=3, decimal_places=1)
    RealEffort = models.DecimalField(max_digits=3, decimal_places=1)
    PlannedHours = models.DecimalField(max_digits=3, decimal_places=1)
    RealHours = models.DecimalField(max_digits=3, decimal_places=1)
    # State =
    Creation = models.CharField(max_length=50)
    Edition = models.CharField(max_length=50)
    

    class Meta:
        unique_together = ('IterationTaskCode', 'IterationCode', 'ProjectId')   
    
    def __str__(self):
        return "{}|{}".format(self.IterationCode, self.IterationTaskCode)
 
''' Esta creo que ya, revisar lo de si se crean con un planning entry'''
class IterationTaskHistorial(models.Model):
    
    IterationTaskCode = models.ForeignKey(IterationTask, on_delete=models.DO_NOTHING, blank=False)
    IterationCode = models.ForeignKey(Iteration, on_delete=models.DO_NOTHING, blank=False)
    ProjectId = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False)
    
    Date = models.DateTimeField()
    Annotation =  models.CharField(max_length=250)
    # State=
    
    class Meta:
        unique_together = ('IterationTaskCode', 'Date','IterationCode','ProjectId')   
    
    def __str__(self):
        return "{}|Entry:{}".format(self.IterationTaskCode, self.Date)

class TaskProxy(models.Model):
    
    IterationTaskCode = models.OneToOneField(IterationTask, on_delete=models.DO_NOTHING, blank=False)
    IterationCode = models.ForeignKey(Iteration, on_delete=models.DO_NOTHING, blank=False)
    ProjectId = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False)
    
    
    Title =  models.CharField(max_length=50)
    Type =  models.CharField(max_length=50)
    EffortAvg = models.DecimalField(max_digits=3,decimal_places=1)
    
    
    class Meta:
        unique_together = ('IterationTaskCode', 'IterationCode', 'ProjectId')   
    
    def __str__(self):
        return "{}|Effort:{}".format(self.IterationTaskCode, self.EffortAvg)

class PlanningEntry(models.Model):
  
    PlanningEntryId = models.AutoField(primary_key=True)
    IterationTaskCode = models.ForeignKey('IterationTask', on_delete=models.DO_NOTHING, blank=False)
    IterationCode = models.ForeignKey('Iteration', on_delete=models.DO_NOTHING, blank=False)
    ProjectId = models.ForeignKey('Project',on_delete=models.DO_NOTHING, blank=False)
    
    Creation = models.CharField(max_length=50)
    Edition = models.CharField(max_length=50)
    PlannedHours = models.DecimalField(max_digits=3 ,decimal_places=1)
    RealHours = models.DecimalField(max_digits=3 ,decimal_places=1)
    PlannedEffort= models.DecimalField(max_digits=3 ,decimal_places=1)
    RealEffort = models.DecimalField(max_digits=3 ,decimal_places=1)
    # State =
    Anotation =  models.CharField(max_length=250)
    Document = models.ForeignKey('TeamMember' ,on_delete=models.DO_NOTHING, blank=False)
   
    class Meta:
        unique_together = ('IterationTaskCode', 'PlanningEntryId', 'IterationCode', 'ProjectId')   
    
    
    def __str__(self):
        return "PlanningEntry: {}| Assigned to:{}".format(self.IterationTaskCode,self.Document)
 
'''
class PlanningPeriod(models.Model):
  
   PeriodId = models.AutoField(primary_key=True)
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
    
''' 
class TeamMember(models.Model):
    
    Document = models.CharField(primary_key=True, max_length=50)
    
    Names =  models.CharField(max_length=100)
    Mail =  models.CharField(max_length=100)
    
    ProxyFactor = models.DecimalField(max_digits=3,decimal_places=1)
    AvailableWeekHours = models.DecimalField(max_digits=3,decimal_places=1)
    Active = models.BooleanField()
    
    def __str__(self):
        return "{}|{}|{}".format(self.Document,self.Names,self.Active)
