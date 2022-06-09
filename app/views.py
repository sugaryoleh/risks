from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import CompanyRisk, Asset


class RiskCreateView(CreateView):
    model = CompanyRisk
    fields = '__all__'
    success_url = reverse_lazy('risk-list')


class RiskUpdateView(UpdateView):
    model = CompanyRisk
    fields = '__all__'


class RiskDeleteView(DeleteView):
    model = CompanyRisk
    success_url = reverse_lazy('risk-list')


def risk_list(request):
    objects = CompanyRisk.objects.all()

    return render(request, template_name='app/risk_list.html', context={'objects':objects})


def check(asset_name, danger):
    asset_names = ['server', 'personal_data', 'contract']
    dangers = [d[0].lower() for d in CompanyRisk.DangerType.choices]
    if asset_name in asset_names and danger in dangers:
        return True
    return False


def detail_risk_list(request, asset_name, danger):
    if not check(asset_name, danger):
        return HttpResponse('Bad request')
    objects = CompanyRisk.objects
    if asset_name == 'server':
        objects = objects.filter(asset__name='Server')
    elif asset_name == 'personal_data':
        objects = objects.filter(asset__name='Personal data')
    else:
        objects = objects.filter(asset__name='Company contracts')
    if danger == 'accessibility':
        objects = objects.filter(danger_type='Accessibility')
    elif danger == 'accessibility':
        objects = objects.filter(danger_type='Confidentiality')
    else:
        objects = objects.filter(danger_type='Integrity')
    return render(request, template_name='app/risk_detail_list.html', context={'objects':objects})

