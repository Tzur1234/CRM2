from django.contrib import admin
from django.urls import path, include
from leads import views

app_name="leads"
urlpatterns = [
    path('', views.LeadListView.as_view(), name="leads"),
    path('create-lead/', views.LeadCreateView.as_view(), name="create-lead"),
    path('detail-lead/<int:pk>/', views.LeadDetailView.as_view(), name="detail-lead"),
    path('update-lead/<int:pk>/', views.LeadUpdateView.as_view(), name="update-lead"),
    path('delete-lead/<int:pk>/', views.LeadDeleteView.as_view(), name="delete-lead"),
]
