# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.


def index(request):
    projects = Project.get_projects()
    return render(request, 'all-projects/index.html', {"projects": projects})


def project(request, project - id):

    try:
        project = Project.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'all-projects/project.html', {"project": project})
