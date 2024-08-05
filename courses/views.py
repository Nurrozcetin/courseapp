from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from courses.forms import CourseCreateForm, UploadForm
from .models import Course, Slider, UploadModel
from .models import Category
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):
    courses = Course.objects.filter(isActive = 1, isHome=1)
    categories = Category.objects.all()
    sliders = Slider.objects.filter(is_active=True)

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
        'sliders': sliders
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

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/courses")
    else:
        form = CourseCreateForm()
    return render(request, "courses/create-course.html", {"form":form})

@user_passes_test(isAdmin)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses': courses,
    })

@user_passes_test(isAdmin)
def course_edit(request, id):
    edit_course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES, instance=edit_course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseCreateForm(instance=edit_course)
    
    return render(request, "courses/edit-course.html", {"form":form})

@user_passes_test(isAdmin)
def course_delete(request, id):
    delete_course = get_object_or_404(Course, pk=id)

    if request.method=="POST":
        delete_course.delete()
        return redirect("course_list")
    else:
         return render(request, "courses/course-delete.html", {"course":delete_course})

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image = request.FILES["image"])
            model.save()
            return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", {"form":form})

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

def details(request, slug):
    course_details = get_object_or_404(Course, slug = slug)
    context = {
        'course':course_details
    }
    return render(request, "course/details.html", context)