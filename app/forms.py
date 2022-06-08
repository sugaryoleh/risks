from django.forms import ModelForm
from .models import CompanyRisk


class CompanyRiskCreateRetrieveUpdateForm(ModelForm):
    class Meta:
        model = CompanyRisk
        fields = ['asset', 'danger_type', 'danger', 'danger_source', 'implementation_mechanism']

