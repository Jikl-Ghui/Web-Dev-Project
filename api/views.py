from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Category, Task, Submission
from .serializers import (
    CategorySerializer, TaskSerializer, 
    TaskStatSerializer, SubmissionSerializer
)

# --- FBV (Требование: минимум 2) ---

@api_view(['GET'])
def get_project_info(request):
    return Response({"project": "Code Trainer KBTU", "version": "1.0"})

@api_view(['GET'])
def get_stats(request):
    data = {'total_tasks': Task.objects.count(), 'difficulty_level': 'Mixed'}
    serializer = TaskStatSerializer(data)
    return Response(serializer.data)

# FBV для логина (удобно для фронтенда)
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

# --- CBV (Требование: минимум 2) ---

class CategoryListCBV(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class TaskListByCategoryCBV(APIView):
    def get(self, request, category_id):
        tasks = Task.objects.filter(category_id=category_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

# --- Full CRUD для Submission (используем Generics для скорости) ---

class SubmissionListCreateAPIView(generics.ListCreateAPIView):
    """Просмотр своих решений и отправка нового (Create + Read)"""
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Привязываем submission к текущему юзеру (Requirement!)
        serializer.save(user=self.request.user)

class SubmissionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, обновление и удаление конкретного решения (Read + Update + Delete)"""
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)