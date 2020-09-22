from django.urls import path
from . import views

urlpatterns = [
    path('', views.allProjects, name='projects'),
    path('<int:project_id>/', views.projectDetail, name='projectDetail')
]
