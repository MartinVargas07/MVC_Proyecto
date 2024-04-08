from django.urls import path
from . import views

app_name = 'academico'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso)

]