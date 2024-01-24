from django.urls import path, include
from rest_framework import routers
from api.todo_list.controllers.todo_list import TodoListViewSet

router = routers.DefaultRouter()
router.register(r'todo-lists', TodoListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
