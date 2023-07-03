from rest_framework import generics
from api.models import TodoItem
from api.serializers import TodoItemSerializer

# Inheritance GenericAPIView,ListModelMixin,CreateModelMixin
class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Inheritance GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
class TodoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer