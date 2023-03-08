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
    path('assign-lead/<int:pk>/', views.AssignLeadView.as_view(), name="assign-lead"),

    path('category-lead/', views.CategoryListView.as_view(), name="category-lead"),
    path('category-specific/<int:pk>/', views.SpecificCategoryView.as_view(), name="category-specific"),
    path('category-create/', views.CreateCategoryView.as_view(), name="category-create"),
    path('category-update/<int:pk>/', views.UpdateCategoryView.as_view(), name="category-update"),
    path('category-delete/<int:pk>/', views.DeleteCategoryView.as_view(), name="category-delete"),
    path('category-assign-lead-to-category/', views.AssignLeadToCategory.as_view(), name="category-assign-lead-to-category"),
]
