from django.urls import path

from main.views import CreateToDoGenericAPIView, CurrentToDoGenericAPIView, CompletedToDoGenericAPIView, \
    UpdateDestroyToDoGenericAPIView, ToDoDetailGenericAPIVIew

urlpatterns = [
    path('create-todo', CreateToDoGenericAPIView.as_view(), name='create-todo'),
    path('current-todo', CurrentToDoGenericAPIView.as_view(), name='current-todo'),
    path('completed-todo', CompletedToDoGenericAPIView.as_view(), name='complete-todo'),
    path('todo-detail/<int:todo_id>', ToDoDetailGenericAPIVIew.as_view(), name='todo-detail'),
    path('update-destroy-todo/<int:todo_id>', UpdateDestroyToDoGenericAPIView.as_view(), name='update-destroy-todo'),

]