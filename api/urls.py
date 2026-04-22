from django.urls import path
from .views import (
    get_project_info, get_stats, login_view,
    CategoryListCBV, TaskListByCategoryCBV,
    SubmissionListCreateAPIView, SubmissionDetailAPIView
)

urlpatterns = [
    # Auth
    path('login/', login_view),
    
    # Information & Stats (FBV)
    path('info/', get_project_info),
    path('stats/', get_stats),
    
    # Categories & Tasks (CBV)
    path('categories/', CategoryListCBV.as_view()),
    path('categories/<int:category_id>/tasks/', TaskListByCategoryCBV.as_view()),
    
    # Submissions (Full CRUD)
    path('submissions/', SubmissionListCreateAPIView.as_view()),
    path('submissions/<int:pk>/', SubmissionDetailAPIView.as_view()),
]