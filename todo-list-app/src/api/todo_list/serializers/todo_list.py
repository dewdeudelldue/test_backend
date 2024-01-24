from rest_framework import serializers
from api.todo_list.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = "__all__"