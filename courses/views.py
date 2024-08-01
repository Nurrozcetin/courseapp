from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course
from .models import Category

def index(request):
    courses = Course.objects.filter(isActive = 1, isHome=1)
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses
    })

def search(request):
    if "q" in request.GET and request.GET["q"] != " ":
        q = request.GET["q"]
        q_course = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        q_category = Category.objects.all()
    else:
        return redirect("/courses")

    return render(request, 'courses/search.html', {
        'categories': q_category,
        'courses': q_course,
    })

# def details(request, slug):
#     course = get_object_or_404(Course, slug=slug)

#     context = {
#         'course': course
#     }
#     return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    course = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    category = Category.objects.all()

    paginator = Paginator(course, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    print(page_obj.paginator.num_pages)

    return render(request, 'courses/list.html', {
        'categories': category,
        'page_obj': page_obj,
        'choosenCategory': slug
    })