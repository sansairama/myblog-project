from django.shortcuts import render
from .models import job
def  home(request):
    work=job.objects
    return render(request, 'jobs/home.html', {'work':work})
