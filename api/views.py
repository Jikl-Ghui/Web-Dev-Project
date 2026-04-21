from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer, TaskStatSerializer

# --- 2 Function-Based Views (FBV) ---
@api_view(['GET'])
def get_project_info(request):
    return Response({"project": "Code Trainer KBTU", "version": "1.0"})

@api_view(['GET'])
def get_stats(request):
    data = {'total_tasks': Task.objects.count(), 'difficulty_level': 'Mixed'}
    serializer = TaskStatSerializer(data)
    return Response(serializer.data)

# --- 2 Class-Based Views (CBV) ---
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