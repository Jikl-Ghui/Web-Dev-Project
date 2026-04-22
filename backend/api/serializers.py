from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Task, Submission


# --- serializers.Serializer (2 required) ---

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )


class SubmissionCreateSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    code = serializers.CharField()
    language = serializers.ChoiceField(choices=['python', 'javascript', 'java', 'cpp'])

    def validate_task_id(self, value):
        if not Task.objects.filter(id=value).exists():
            raise serializers.ValidationError("Task not found.")
        return value

    def create(self, validated_data):
        import random
        status = random.choice(['accepted', 'wrong'])
        return Submission.objects.create(
            user=self.context['request'].user,
            task_id=validated_data['task_id'],
            code=validated_data['code'],
            language=validated_data['language'],
            status=status,
        )


# --- serializers.ModelSerializer (2 required) ---

class CategorySerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'task_count']

    def get_task_count(self, obj):
        return obj.tasks.count()


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'examples', 'difficulty', 'category', 'category_name', 'created_at']


class SubmissionSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(source='task.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Submission
        fields = ['id', 'task', 'task_title', 'username', 'code', 'language', 'status', 'submitted_at', 'updated_at']
        read_only_fields = ['user', 'status', 'submitted_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
