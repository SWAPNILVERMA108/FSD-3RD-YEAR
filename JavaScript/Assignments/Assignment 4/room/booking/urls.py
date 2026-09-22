from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.home, name='home'),
    path('classrooms/<int:classroom_id>/reserve/', views.reserve, name='reserve'),
    path('booking/<str:code>/', views.confirmation, name='confirmation'),
]
