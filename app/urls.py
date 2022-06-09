from django.urls import path
from .views import RiskCreateView, RiskUpdateView, RiskDeleteView, risk_list, detail_risk_list

urlpatterns = [
    # ...update
    path('risks/add/', RiskCreateView.as_view(), name='risk-add'),
    path('risks/<int:pk>/', RiskUpdateView.as_view(), name='risk-update'),
    path('risks/<int:pk>/delete/', RiskDeleteView.as_view(), name='risk-delete'),
    path('risks/', risk_list, name='risk-list'),
    path('risks/<str:asset_name>/<str:danger>/', detail_risk_list, name='risk-list-detail')
]
