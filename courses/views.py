from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from courses.forms import CourseCreateForm
from .models import Course
from .models import Category
import random
import os

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

def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/courses")
    else:
        form = CourseCreateForm()
    return render(request, "courses/create-course.html", {"form":form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses': courses,
    })

def course_edit(request, id):
    edit_course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseCreateForm(request.POST, instance=edit_course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseCreateForm(instance=edit_course)
    
    return render(request, "courses/edit-course.html", {"form":form})


def course_delete(request, id):
    delete_course = get_object_or_404(Course, pk=id)

    if request.method=="POST":
        delete_course.delete()
        return redirect("course_list")
    else:
         return render(request, "courses/course-delete.html", {"course":delete_course})

def upload(request):
    if request.method == "POST":
        uploaded_images = request.FILES.getlist("images")
        for file in uploaded_images:
            handle_uploaded_files(file)
        return render(request, "courses/success.html")
    return render(request, "courses/upload.html")

def handle_uploaded_files(file):
    number = random.randint(1,99999)
    filename, file_extention = os.path.splitext(file.name)
    name = filename + "_" + str(number) + file_extention
    with open("uploads/" + name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

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

    return render(request, 'courses/list.html', {
        'categories': category,
        'page_obj': page_obj,
        'choosenCategory': slug
    })