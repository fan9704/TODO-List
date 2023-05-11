from django.urls import path,include
from api.views import apiView, genericsConcreteView,genericsViewSet, viewSets, mixins
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

# Generic ViewSet
router = DefaultRouter()
router.register('todo', genericsViewSet.TodoViewSet, basename='todoGeneric')

# router2 = SimpleRouter()
# router2.register('todo', viewSets.TodoViewSet, basename='todoViewSet')

urlpatterns = [
    # GenericViewSet
    path('genericViewSet/', include(router.urls)),
    # ViewSet
    # path('ViewSet/', include(router2.urls)),
    path('viewSets/', viewSets.TodoViewSet.as_view({
        'get': 'list',
        'post':'create'
    })),
    path('viewSets/<int:pk>/', viewSets.TodoViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "patch":"partial_update",
        "delete":"destroy"
    })),
    # APIView
    path('apiView/', apiView.TodoList.as_view(), name='todo_list_api'),
    path('apiView/<int:pk>/', apiView.TodoDetail.as_view(), name='todo_detail_api'),
    # GenericConcreteView GenericAPIView + ModelMixin
    path('genericView/', genericsConcreteView.TodoItemList.as_view(), name='todo-list'),
    path('genericView/<int:pk>/', genericsConcreteView.TodoItemDetail.as_view(), name='todo-detail'),
    # Mixin
    path('mixin/', mixins.TodoListAPIView.as_view(), name='todo_list_create'),
    path('mixin/<int:pk>/', mixins.TodoDetailAPIView.as_view(), name='todo_detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)