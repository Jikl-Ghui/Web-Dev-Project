from django.contrib import admin
from .models import Category, Task, Submission

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Submission)
