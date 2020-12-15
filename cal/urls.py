from django.urls import path
from .import views

app_name = "cal"
urlpatterns = [
    path('', views.index, name='home'),
    path('calendar/', views.calendarview.as_view(), name='calendar'),
    path('newevent/', views.event, name='newevent'),
    path('editevent/', views.event, name='editevent'),  
]