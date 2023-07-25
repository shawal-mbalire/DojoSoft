from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo, User
from .serialisers import TodoSerializer

@api_view(['GET'])
def getAllTodos(request):
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
@api_view(['POST','GET'])
def createUserTodo(request):
    serialiser = TodoSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

# read
@api_view(['GET'])
def getUserTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

# update
@api_view(['POST'])
def updateUserTodo(request):
    pass

# delete
@api_view(['GET'])
def deleteUserTodo(request):
    pass
