from django.urls import path
from up_validate import views , validar_txt
 


urlpatterns = [
    path('validar_csv/', views.validar_csv, name='validar_csv'),
    path('validar_txt/', validar_txt, name='validar_txt'),
]
