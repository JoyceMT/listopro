from django.db import models

from candidates.models import Candidate
from jobs.models import Job

# Create your models here.
class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

