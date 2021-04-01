from django.shortcuts import render
from .models import Application
from candidates.models import Candidate

# Create your views here.
def applications_list_view(request):
    application_objects = Application.objects.filter(
      candidate=Candidate.objects.get(id=1)).all()
    context = {
      'application_objects': application_objects
    }
    return render(request, 'applications/index.html', context)
