from django.db import models
from django.contrib.auth.models import User

# Кастомный менеджер для задач (Bonus Points!)
class TaskManager(models.Manager):
    def get_hard_tasks(self):
        return self.filter(difficulty='Hard')

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Task(models.Model):
    DIFFICULTY_CHOICES = [('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')]
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')

    # Подключаем кастомный менеджер
    objects = TaskManager()

    def __str__(self):
        return self.title

class Submission(models.Model):
    code = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')

    def __str__(self):
        return f"Submission {self.id} by {self.user.username}"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username