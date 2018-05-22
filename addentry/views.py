from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PhysicianForm
from .models import Physician
# Create your views here.
def index(request):
    return render(request, 'index.html')
def entry(request):
    form = PhysicianForm()
    return render(request, 'entry.html', {'form': form})
def submitEntry(request):
    form = PhysicianForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('view', args=[request.POST['npi']]))
    else:
        return render(request, 'entry.html', {'form': form, 'error': form.errors})
def view(request, physicianId):
    p = get_object_or_404(Physician, pk=physicianId)
    return render(request, 'view.html', {'p': p})


