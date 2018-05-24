from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from business_rules import export_rule_data, run_all
import json
from .forms import PhysicianForm, RuleForm
from .models import Physician, Rule
from .rules import ProductVariables, ProductActions

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
def runRule(request, physicianId):
    p = get_object_or_404(Physician, pk=physicianId)
    objs = Rule.objects.all()
    rules = []
    for obj in objs:
        rules.append(json.loads(obj.content))
    products = Physician.objects.all()
    for product in products:
        run_all(rules, ProductVariables(product),ProductActions(product),False)
    return HttpResponseRedirect(reverse('view', args=[physicianId]))

class list(ListView):
    model = Physician
    template_name = 'list.html'
class ruleList(ListView):
    model = Rule
    template_name = 'ruleList.html'
def newRule(request):
    url = reverse('new-rule')
    data = json.dumps(export_rule_data(ProductVariables, ProductActions))
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rule-list'))
    else:
        form = RuleForm()
    return render(request, 'newRule.html', {'form': form, 'data': data, 'url': url})
def editRule(request, ruleId):
    url = reverse('edit-rule', args=[ruleId])
    data = json.dumps(export_rule_data(ProductVariables, ProductActions))
    rule = get_object_or_404(Rule, pk=ruleId)
    if request.method == 'POST':
        form = RuleForm(request.POST, instance=rule)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rule-list'))
    else:
        form = RuleForm(instance=rule)
    return render(request, 'newRule.html', {'form': form, 'data': data, 'url': url})
