from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import CompanyRisk


class RiskCreateView(CreateView):
    model = CompanyRisk
    fields = '__all__'


class RiskUpdateView(UpdateView):
    model = CompanyRisk
    fields = '__all__'


class RiskDeleteView(DeleteView):
    model = CompanyRisk
    success_url = reverse_lazy('risk-list')


def risk_list(request):
    objects = CompanyRisk.objects.all()

    return render(request, template_name='app/risk_list.html', context={'objects':objects})

