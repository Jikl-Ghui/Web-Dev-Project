from rest_framework import serializers
from .models import Category, Task, Submission
from django.contrib.auth.models import User

# 1. ModelSerializer для категорий
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# 2. ModelSerializer для задач
class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Task
        fields = '__all__'

# 3. Обычный Serializer (требование задания) - для статистики
class TaskStatSerializer(serializers.Serializer):
    total_tasks = serializers.IntegerField()
    difficulty_level = serializers.CharField()

# 4. Обычный Serializer - для краткой инфо о пользователе
class UserShortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()