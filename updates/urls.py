from django.urls import path
from . import views

urlpatterns = [
    path('', views.allUpdates, name='updates'),
    path('<int:update_id>/', views.updateDetail, name = 'updateDetail')
]
