from django.urls import path
from .views import get_project_info, get_stats, CategoryListCBV, TaskListByCategoryCBV

urlpatterns = [
    path('info/', get_project_info),
    path('stats/', get_stats),
    path('categories/', CategoryListCBV.as_view()),
    path('categories/<int:category_id>/tasks/', TaskListByCategoryCBV.as_view()),
]