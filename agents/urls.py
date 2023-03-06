from django.urls import reverse, path
from agents import views


app_name='agents'

urlpatterns = [
    path('agent-list/', views.AgentListView.as_view(), name="agent-list"),
    path('agent-create/', views.AgentCreateView.as_view(), name="agent-create"),
    path('detail-agent/<int:pk>/', views.AgentDetailView.as_view(), name="detail-agent"),
    path('update-agent/<int:pk>/', views.AgentUpdateView.as_view(), name="update-agent"),
    path('delete-agent/<int:pk>/', views.AgentDeleteView.as_view(), name="delete-agent"),
]

