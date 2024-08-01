from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Course
from .models import Category

def index(request):
    courses = Course.objects.filter(isActive = 1)
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    course = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    category = Category.objects.all()

    paginator = Paginator(course, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    print(page_obj.paginator.num_pages)

    return render(request, 'courses/index.html', {
        'categories': category,
        'page_obj': page_obj,
        'choosenCategory': slug
    })