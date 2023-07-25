from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllTodos),
    path('add_gen/', views.addTodo),

    # paths for crud
    path('add/', views.createUserTodo),
    path('read/', views.getUserTodos),
    path('update/', views.updateUserTodo),
    path('delete/', views.deleteUserTodo),

]
