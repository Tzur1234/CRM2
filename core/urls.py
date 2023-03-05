from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
import leads
from leads import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DashboardPageView.as_view(), name="dashboard"),
    path('base/', views.BasePageView.as_view(), name="base"),
    path('leads/', include('leads.urls')),
]



# make static files avialable when debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )   

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    







