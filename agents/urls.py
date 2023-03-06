from django.urls import reverse, path
from agents import views


app_name='agents'

urlpatterns = [
    path('agent-list/', views.AgentListView.as_view(), name="agent-list"),
    path('agent-create/', views.AgentCreateView.as_view(), name="agent-create"),
]
