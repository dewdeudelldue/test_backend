from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import ParseError, NotFound, PermissionDenied, MethodNotAllowed
from api.todo_list.models.todo_list import TodoList
from api.todo_list.serializers.todo_list import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer