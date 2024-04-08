from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
    path('edicionCurso/<str:codigo>/', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),
    path('eliminarCurso/<str:codigo>/', views.eliminarCurso, name='eliminarCurso'),
    path('academico/login/', views.login_view, name='login'),
    path('academico/protected/', views.protected_view, name='protected_page'),
]