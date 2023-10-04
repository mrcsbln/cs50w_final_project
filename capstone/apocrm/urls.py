from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('patient_record/<int:pk>', views.patient_record, name='patient_record'),
    path('delete_patient_record/<int:pk>', views.delete_patient_record, name='delete_patient_record'),
    path('add_patient_record/', views.add_patient_record, name='add_patient_record'),
    path('edit_patient_record/<int:pk>', views.edit_patient_record, name='edit_patient_record'),
    path('search/', views.search, name='search'),
]