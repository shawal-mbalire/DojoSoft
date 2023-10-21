from rest_framework import generics
from base.models    import Todo
from .serialisers   import TodoSerializer
from .mixins        import UserQueryMixin
from django.contrib.auth import get_user

# TODOs CRUD
class TodoDetailAPIView(UserQueryMixin,generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
class TodoListCreateAPIView(UserQueryMixin,generics.ListCreateAPIView,):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        user = self.request.user
        request.data._mutable = True
        request.data['user'] = get_user(self.request)
        request.data._mutable = False
        return super().create(request, *args, **kwargs)

class TodoUpdateAPIView(UserQueryMixin,generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

class TodoDestroyAPIView(UserQueryMixin,generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'