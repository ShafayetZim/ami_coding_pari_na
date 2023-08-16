from django.urls import path
from . import views

urlpatterns = [
    path('khoj_search/', views.khoj_search, name='khoj_search'),
    path('api/get_input_values/', views.get_input_values_api, name='get_input_values_api'),
]
