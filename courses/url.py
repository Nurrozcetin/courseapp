from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('list/', views.courses ),
    path('<course_name>', views.details),
    path('course/<int:category_id>', views.getCoursesByCategoryId),
    path('course/<str:category_name>', views.getCoursesByCategory),
]