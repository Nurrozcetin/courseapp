from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('search/', views.search, name="search"),
    #path('<slug:slug>', views.details),
    path('category/<slug:slug>', views.getCoursesByCategory, name='courses_by_category')
]