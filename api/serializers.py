from rest_framework import serializers
from api.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'created_at', 'updated_at', 'title', 'completed')