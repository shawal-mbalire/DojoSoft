from django.urls import path
from . import views

urlpatterns = [
    path('users', views.readUsers, name='readUsers'),
    path('todos', views.readTodos, name='readTodos'),

    # paths for todo crud
    path('todo/create', views.createUserTodo,name='createUserTodo'),
    path('todo/read'  , views.readUserTodos,name='readUserTodos'),
    path('todo/update', views.updateUserTodo,name='updateUserTodo'),
    path('todo/delete', views.deleteUserTodo,name='deleteUserTodo'),

    # paths for user crud
    path('user/create', views.createUser,name='createUser'    ),
    path('user/read'  , views.readUser,name='readUser'),
    path('user/update/<str:uuid>', views.updateUser, name='updateUser'),
    path('user/delete', views.deleteUser,name='deleteUser'),

]
