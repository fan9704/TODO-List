from rest_framework import viewsets
from rest_framework.response import Response

from api.models import TodoItem
from api.serializers import TodoItemSerializer

class TodoViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = TodoItem.objects.all()
        serializer = TodoItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        try:
            todo = TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            return Response(status=404)
        
        serializer = TodoItemSerializer(todo)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        try:
            todo = TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            return Response(status=404)
        
        serializer = TodoItemSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def partial_update(self, request, pk=None):
        try:
            todo = TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            return Response(status=404)
        
        serializer = TodoItemSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        try:
            todo = TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            return Response(status=404)
        
        todo.delete()
        return Response(status=204)