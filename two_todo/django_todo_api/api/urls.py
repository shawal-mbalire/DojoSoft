from django.urls import path
from . import views

urlpatterns = [
    path('users', views.readUsers),
    path('todos', views.readTodos),

    # paths for todo crud
    path('todo/create', views.createUserTodo),
    path('todo/read'  , views.readUserTodos),
    path('todo/update', views.updateUserTodo),
    path('todo/delete', views.deleteUserTodo),

    # paths for user crud
    path('user/create', views.createUser    ),
    path('user/read'  , views.readUser),
    path('user/update', views.updateUser),
    path('user/delete', views.deleteUser),

]
