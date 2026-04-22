from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Category, Task, Submission
from .serializers import (
    CategorySerializer, TaskSerializer,
    SubmissionSerializer, SubmissionCreateSerializer
)


# --- FBV (Function Based Views) ---

@api_view(['GET'])
@permission_classes([AllowAny])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def tasks_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
    tasks = Task.objects.filter(category=category)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# --- CBV (Class Based Views) ---

class TaskDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class SubmissionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        submissions = Submission.objects.for_user(request.user)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubmissionCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            submission = serializer.save()
            return Response(SubmissionSerializer(submission).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmissionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, submission_id, user):
        try:
            return Submission.objects.get(id=submission_id, user=user)
        except Submission.DoesNotExist:
            return None

    def get(self, request, submission_id):
        submission = self.get_object(submission_id, request.user)
        if not submission:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(SubmissionSerializer(submission).data)

    def put(self, request, submission_id):
        submission = self.get_object(submission_id, request.user)
        if not submission:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubmissionSerializer(submission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, submission_id):
        submission = self.get_object(submission_id, request.user)
        if not submission:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        submission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
