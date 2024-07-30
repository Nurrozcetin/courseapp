from datetime import date
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programming":"get courses by programming",
    "web-developing":"get courses by web-developing",
    "mobile":"get courses by mobile"
}

db = {
    "courses": [
        {
            "title": "javascript course",
            "desc": "javascript course desc",
            "imageUrl": "webb.jfif",
            "slug": "javascript-course",
            "date": date(2022,10,15), 
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "python course",
            "desc": "python course desc",
            "imageUrl": "pythonn.png",
            "slug": "python-course",
            "date": date(2022,10,15),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "kotlin course",
            "desc": "kotlin course desc",
            "imageUrl": "kotlin.png",
            "slug": "kotlin-course",
            "date": date(2022,10,15),
            "isActive": False,
            "isUpdated": False
        }
    ],
    "categories": [
        { "id": 1, "name": "programming", "slug": "programming"},
        { "id": 2, "name": "web development", "slug": "web development"},
        { "id": 3, "name": "mobile development", "slug": "mobile development"}
    ]
}
def index(request):
    courses = []
    categories = db["categories"]

    for course in db["courses"]:
        if course["isActive"] == True:
            courses.append(course)

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses
    })

def details(request, course_name):
    return HttpResponse(f'{course_name} detail course')


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("<h1>Wrong category</h1>")

def getCoursesByCategoryId(request, category_id):
    category_lists = list(data.keys())
    if(category_id > len(category_lists)):
        return HttpResponseNotFound("wrong category id ")
    
    category_name = category_lists[category_id - 1]

    redirect_url = reverse('courses by category', args=[category_name])
    return redirect(redirect_url)

#return HttpResponse(f'get courses by {category}')