from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_csv, name='home_page'),
    path('success/', views.parsing_request, name='parsing_page'),
    path('success/result/', views.parsing_result, name='result_page'),
    path('success/result/save/', views.save_to_db, name='save_page'),
]

