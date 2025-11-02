from django.urls import path
from django.urls import path
from . import views, views_api

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/toggle/', views.task_toggle, name='task_toggle'),  # toggle completion
# REST API
    path('api/tasks/', views_api.TaskListCreateAPIView.as_view(), name='api_task_list_create'),
    path('api/tasks/<int:pk>/', views_api.TaskRetrieveUpdateDestroyAPIView.as_view(), name='api_task_detail'),

]
