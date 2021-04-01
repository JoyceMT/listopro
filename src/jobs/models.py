from django.db import models

# Create your models here.
class Job(models.Model):
  title = models.CharField(max_length=100)
  job_description = models.TextField()
  company_description = models.TextField()
  requirements = models.TextField()
  location = models.CharField(choices=(('onsite', 'On-site'), ('remote', 'Remote'),), max_length=50, blank=True, null=True)
  salary = models.CharField(choices=(('negociable', 'Negociable'), ('competitivo', 'Competitivo'),), max_length=50, blank=True, null=True)

  def __str__(self):
    return self.title
