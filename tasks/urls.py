from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),#criada rota que atribui o numero do id ao endereço
    #será criada uma view que vai pegar esse número.
    path('yourname/<str:name>', views.yourName, name='your-name')
]