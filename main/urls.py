from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.index,name='index'),
    path('patients/<str:id>/',views.view_patient,name ='view_patient'),
    path('add/', views.add, name='add'),
    path('edit/<str:id>/',views.edit,name ='edit'),
    path('delete/<str:id>/',views.delete, name='delete'),
    path('wards/',views.wards,name='wards'),
]
