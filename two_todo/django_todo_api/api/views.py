from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo, User
from .serialisers import TodoSerializer, UserSerializer

# get all users and get all todos
@api_view(['GET'])
def readTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def readUsers(request):
    todos = User.objects.all()
    serializer = UserSerializer(todos, many=True)
    return Response(serializer.data)




# user must be able to CRUD their todos
@api_view(['POST','GET'])
def createUserTodo(request):
    serialiser = TodoSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)
@api_view(['GET'])
def readUserTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)
@api_view(['POST','GET'])
def updateUserTodo(request):
    pass
@api_view(['GET','GET'])
def deleteUserTodo(request):
    pass





# admin must crud the users
@api_view(['POST','GET'])
def createUser(request):
    serialiser = UserSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)
@api_view(['POST','GET'])
def readUser(request):
    todos = User.objects.all()
    serializer = UserSerializer(todos, many=True)
    return Response(serializer.data)
@api_view(['POST','GET'])
def updateUser(request):
    pass
@api_view(['POST','GET'])
def deleteUser(request):
    pass
