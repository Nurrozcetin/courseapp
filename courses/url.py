from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('list/', views.courses ),
    path('<course_name>', views.details),
    path('programming/', views.programming),
    path('apps/', views.apps),
    path('category/<int:category_id>', views.getCoursesByCategoryId),
    path('category/<str:category_name>', views.getCoursesByCategoryName),
]