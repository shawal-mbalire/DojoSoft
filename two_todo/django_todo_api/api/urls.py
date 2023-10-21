from .                              import views
from django.urls                    import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    
    path('todos/<int:pk>'        , views.TodoDetailAPIView    .as_view(),name='todo-detail'),
    path('todos/'                , views.TodoListCreateAPIView.as_view(),name='todo-list-create'),
    path('todos/update/<int:pk>/', views.TodoUpdateAPIView    .as_view(),name='todo-delete'),
    path('todos/delete/<int:pk>/', views.TodoDestroyAPIView   .as_view(),name='todo-update'),
]
