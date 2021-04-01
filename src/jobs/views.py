from django.shortcuts import render
from .models import Job
# Create your views here.
def view_job(request, id):
  job = Job.objects.get(id=id)
  context = {
    'job': job
  }

  return render(request, 'jobs/details.html', context)
