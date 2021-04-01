from django.shortcuts import render
from .models import Candidate
from django.contrib.auth.models import User

# Create your views here.
def view_candidate(request, id):
  candidate = Candidate.objects.get(id=id)
  context = {
    'candidate': candidate
  }

  return render(request, 'candidates/details.html', context)
