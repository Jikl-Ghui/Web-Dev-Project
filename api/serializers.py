from rest_framework import serializers
from .models import Category, Task, Submission, StudentProfile
from django.contrib.auth.models import User

# --- ModelSerializers (Требование ТЗ: минимум 2) ---

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    # Добавляем имя категории, чтобы фронту было легче отображать, а не только ID
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'difficulty', 'category', 'category_name']

class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    task_title = serializers.ReadOnlyField(source='task.title')

    class Meta:
        model = Submission
        fields = ['id', 'code', 'status', 'task', 'task_title', 'user', 'created_at']

    # Валидация (добавляет профессионализма вашему коду)
    def validate_code(self, value):
        if not value.strip():
            raise serializers.ValidationError("Код решения не может быть пустым.")
        if len(value) < 10:
            raise serializers.ValidationError("Код слишком короткий для решения задачи.")
        return value

# --- Обычные Serializers (Требование ТЗ: минимум 2) ---

class TaskStatSerializer(serializers.Serializer):
    total_tasks = serializers.IntegerField()
    difficulty_level = serializers.CharField()
    categories_count = serializers.IntegerField()

class UserShortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()