# TODO-List

> Class Base Views Template

---

## APIView

```python=
class TodoList(APIView):
    def get(self, request):
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)
```

---

## ViewSets

```python=
class TodoViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = TodoItem.objects.all()
        serializer = TodoItemSerializer(queryset, many=True)
        return Response(serializer.data)
```

---

## GenericViewSet

```python=
class TodoViewSet(viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoItemSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```

---

## Mixin

```python=
class TodoListAPIView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
```

---

## GenericsConcreteView
 
**ListCreateAPIView** Inheritance GenericAPIView,ListModelMixin,CreateModelMixin
```python=

class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
```