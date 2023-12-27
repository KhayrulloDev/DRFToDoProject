from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from main.models import ToDo
from main.serializers import ToDoSerializer, CurrentToDoSerializer, CompletedToDoSerializer, UpdateToDoSerializer, \
    ToDoDetailSerializer
from rest_framework.response import Response


class CreateToDoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)})


class CurrentToDoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CurrentToDoSerializer

    def get(self, request):
        try:
            current_todo = ToDo.objects.filter(completed=False, user=request.user).order_by('id')
            serializer = self.get_serializer(current_todo, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": str(e)})

class CompletedToDoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompletedToDoSerializer

    def get(self, request):
        try:
            completed_todo = ToDo.objects.filter(completed=True, user=request.user).order_by('id')
            serializer = self.get_serializer(completed_todo, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": e})


class ToDoDetailGenericAPIVIew(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoDetailSerializer

    def get(self, request, todo_id):
        try:
            todo = ToDo.objects.filter(id=todo_id, user=request.user).first()
            serializer = self.get_serializer(todo)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": str(e)})


class UpdateDestroyToDoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateToDoSerializer

    def patch(self, request, todo_id):
        try:
            todo = ToDo.objects.filter(id=todo_id, user=request.user).first()
            serializer = self.get_serializer(todo, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": e})

    def delete(self, request, todo_id):
        try:
            todo = ToDo.objects.filter(id=todo_id, user=request.user).first()
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
