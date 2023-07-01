from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from api.models import TodoItem as Todo
from api.serializers import TodoItemSerializer


class TodoViewSet(viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoItemSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(todo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        todo = self.get_object()
        serializer = self.get_serializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        todo = self.get_object()
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)