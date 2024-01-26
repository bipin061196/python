from django.shortcuts import render, redirect
from .models import Server, Specification
from .forms import  ServerForm, SpecificationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'devops/index.html')

@login_required
def servers(request):
    servers = Server.objects.filter(owner=request.user).order_by('date')
    context = {'servers': servers}
    return render(request, 'devops/servers.html', context)

@login_required
def server(request,server_id):
    server = Server.objects.get(id=server_id)
    if server.owner != request.user:
        raise Http404
    specifications = server.specification_set.order_by('-date')
    context = {'specifications':specifications, 'server':server}
    return render(request, 'devops/specification.html', context)

@login_required
def new_server(request):
    if request.method != 'POST':
        form = ServerForm()
    else:
        form = ServerForm(data=request.POST)
        if form.is_valid():
            #form.save()
            new_server = form.save(commit=False)
            new_server.owner = request.user
            new_server.save()
            return redirect('devops:servers')
    context = {'form':form}
    return render(request, 'devops/new_server.html', context)

@login_required
def new_specification(request, server_id):
    server = Server.objects.get(id=server_id)
    if server.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = SpecificationForm()
    else:
        form = SpecificationForm(data=request.POST)
        if form.is_valid():
            new_specification = form.save(commit=False)
            new_specification.server = server
            new_specification.save()
            return redirect('devops:server', server_id=server_id)
    context = {'server': server, 'form':form}
    return render(request, 'devops/new_specification.html', context)


def edit_specification(request, specification_id):
    specification = Specification.objects.get(id=specification_id)
    server = specification.server
    if request.method != 'POST':
        form = SpecificationForm(instance=specification)
    else:
        form = SpecificationForm(instance=specification, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('devops:server', server_id=server.id)
    context = {'specification':specification, 'server':server, 'form':form}
    return render(request, 'devops/edit_specification.html', context)
        