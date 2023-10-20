from django.urls import path
from . import views

urlpatterns = [
    path('users', views.readUsers, name='readUsers'),
    path('todos', views.readTodos, name='readTodos'),

    # paths for todo crud
    path('todo/create', views.createUserTodo,name='createUserTodo'),
    path('todo/read/<int:user_id>'  , views.readUserTodos,name='readUserTodos'),
    path('todo/update/<int:todo_id>', views.updateUserTodo,name='updateUserTodo'),
    path('todo/delete/<int:todo_id>', views.deleteUserTodo,name='deleteUserTodo'),

    # paths for user crud
    #path('user/create', views.createUser,name='createUser', ),
    #path('user/login'  , views.loginUser,name='loginUser'),
    path('user/update/<int:user_id>', views.updateUser, name='updateUser'),
    path('user/delete/<int:user_id>', views.deleteUser,name='deleteUser'),




    path('users/<int:id>',views.UserDetailAPIView.as_view()),
    path('users/',views.UserListCreateAPIView.as_view()),
    path('users/update/<int:id>/',views.UserUpdateAPIView.as_view()),
    path('users/delete/<int:id>/',views.UserDestroyAPIView.as_view()),



]
