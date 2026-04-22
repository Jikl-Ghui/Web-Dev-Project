from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_list),
    path('categories/<int:category_id>/tasks/', views.tasks_by_category),
    path('tasks/<int:task_id>/', views.TaskDetailView.as_view()),
    path('submissions/', views.SubmissionView.as_view()),
    path('submissions/<int:submission_id>/', views.SubmissionDetailView.as_view()),
]
