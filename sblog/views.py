from django.shortcuts import render, get_object_or_404
from .models import sb

def allblogs(request):
    sblog=sb.objects
    return render(request, 'sblog/allblogs.html',{'sblog':sblog})

def detail(request, sblog_id):
    detailsblog=get_object_or_404(sb, pk=sblog_id)
    return render(request, 'sblog/detail.html', {'sblog':detailsblog} )
