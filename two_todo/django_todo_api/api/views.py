from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo, User
from .serialisers import TodoSerializer

@api_view(['GET'])
def getData(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTodo(request):
    serialiser = TodoSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

# user must be able to CRUD

# create

# read

# update

# delete
