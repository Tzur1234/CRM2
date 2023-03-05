from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
import leads
from leads import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomePageView.as_view(), name="home_page"),
    path('', views.DashboardPageView.as_view(), name="dashboard"),
    path('leads/', include('leads.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]



# make static files avialable when debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )   

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    







