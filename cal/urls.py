from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cal'

urlpatterns = [
    path('', views.calendar_view, name="calendar"),
    path('event/new/', views.event, name="new"),
    path('event/edit/<int:event_id>', views.event, name="edit"),
]
