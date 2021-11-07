from django.contrib import admin
from django.urls import path, include
from pybo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), 
    path('main/', include('main.urls')), 
    path('common/', include('common.urls')),
    path('', include('starrt.urls')),
    path('king/', include('king.urls')),
    path('cal/', include('cal.urls')),
    path('talk/', include('talk.urls')), 
]