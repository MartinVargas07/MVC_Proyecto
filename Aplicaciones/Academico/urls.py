from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
    path('edicionCurso/<str:codigo>/', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),
    path('eliminarCurso/<str:codigo>/', views.eliminarCurso, name='eliminarCurso'),
    path('login/', views.login_view, name='login'),
    path('protected/', views.protected_view, name='protected_page'),
]