from django.urls import path
from up_validate import views


urlpatterns = [
    path('validar_csv/', views.validar_csv, name='validar_csv'),
]
