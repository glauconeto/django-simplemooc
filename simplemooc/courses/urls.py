from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/detalhes/', views.details, name='details'),
    path('<slug:slug>/inscricao/', views.announcements, name='announcements'),
    path('<slug:slug>/anuncios/<int:pk>/', views.show_announcements, 
        name='show_announcements'),
    path('<slug>/inscrição/', views.enrrollment, name='enrrollment'),
    path('<slug:slug>/cancelar-inscricao/', views.undo_enrollment, 
        name='undo_enrollment'),
    path('<slug:slug>/aulas/', views.lessons, name='lessons'),
    path('<slug:slug>/aula/<int:pk>/', views.show_lesson, name='show_lesson'),
    path('<slug:slug>/materiais/<int:pk>/', views.material, name='material')
]