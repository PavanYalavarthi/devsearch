from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projectList = Project.objects.all()
    context = {'projects': projectList}
    return render(request, 'projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request, 'single-project.html', {'project': projectObj })
     
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'project_form.html', context)

def update_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = projectObj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm(instance=projectObj)
    context = {'form': form}
    return render(request, 'project_form.html', context)

def delete_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    if request.method == 'POST':
        projectObj.delete()
        return redirect('projects')
    context = {'object' : projectObj}
    return render(request, 'delete_confirmation_form.html', context)