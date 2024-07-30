from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programming":"get courses by programming",
    "web-developing":"get courses by web-developing",
    "mobile":"get courses by mobile"
}

def index(request):
    return render(request, 'pages/index.html')

def courses(request):
    list_items = ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse('courses by category', args=[category])
        list_items += f"<li><a> href ='{redirect_url}'>{category}</a></li>"
    
    html = f"<h1>courses list</h1><ul>{list_items}</ul>"

    return HttpResponse(html)

def details(request, course_name):
    return HttpResponse(f'{course_name} detail course')

def programming(request):
    return HttpResponse('programming')

def apps(request):
    return HttpResponse('apps')

def getCoursesByCategoryName(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("<h1>Wrong category</h1>")

def getCoursesByCategoryId(request, category_id):
    category_lists = list(data.keys())
    redirect_text = category_lists[category_id - 1]

    if(category_id >= len(category_lists)):
        return HttpResponseNotFound("wrong category id ")
    
    category_name = category_lists[category_id - 1]
    redirect_url = reverse('courses by category', args=[category_name])
    return redirect(redirect_url)

#return HttpResponse(f'get courses by {category}')