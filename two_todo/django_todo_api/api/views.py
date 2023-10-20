from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo, User
from .serialisers import TodoSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework import generics,mixins,permissions,authentication
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import Http404

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.SessionAuthentication]
    lookup_field = 'id'

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class  UserMixingView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args**kwargs)
    def post(self,request,*args,**kwargs):
        pass










@api_view(["GET","POST"])
def product_alt_view(request,id=None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if id != None:
            obj = get_object_or_404(User,id=id)
            data = UserSerializer(obj).data
            return Response(data)        

        queryset = User.objects.all()
        data = UserSerializer(queryset,many=True).data
        return Response(data) 
    if method == "POST":
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response(serializer.errors)




# get all users and get all todos
@api_view(['GET'])
def readTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def readUsers(request):
    todos = User.objects.all()
    serializer = UserSerializer(todos, many=True)
    return JsonResponse(serializer.data)

# user must be able to CRUD their todos
@api_view(['POST','GET'])
def createUserTodo(request):
    serialiser = TodoSerializer(data=request.data)
    if serialiser.is_valid(raise_exception=True):
        serialiser.save()
    return JsonResponse(serialiser.data)

@api_view(['GET'])
def readUserTodos(request,user_id):
    todos = Todo.objects.filter(user_id=user_id)
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def updateUserTodo(request):
    pass

@api_view(['GET','GET'])
def deleteUserTodo(request):
    pass

# admin must crud the users
@api_view(['POST'])
def createUser(request):
    serialiser = UserSerializer(data=request.data)
    if serialiser.is_valid(raise_exception=True):
        serialiser.save()
    return JsonResponse(serialiser.data)

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def loginUser(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return JsonResponse(content)
 


@api_view(['PUT'])
def updateUser(request, uuid):
    user = User.objects.get(id=uuid)
    serialiser = UserSerializer(instance=user,data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return JsonResponse(serialiser.data)


@api_view(['DELETE'])
def deleteUser(request,uuid):
    user = User.objects.get(id=uuid)
    user.delete()
    return JsonResponse('Item Succesfully deleted')

   
# @api_view(['GET'])
# def readUser(request,email,password):
#     todos = User.objects.get(email=email,password=password)
#     serializer = UserSerializer(todos, many=True)
#     return JsonResponse(serializer.data)