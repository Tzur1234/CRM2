from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
import leads
import agents
from leads import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomePageView.as_view(), name="home_page"),
    path('date/', views.LeadJsonView.as_view(), name='json-view'),
    path('', views.DashboardPageView.as_view(), name="dashboard"),
    
    path('agents/', include('agents.urls')),
    path('leads/', include('leads.urls')),

    path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

    
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]



# make static files avialable when debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )   

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    







