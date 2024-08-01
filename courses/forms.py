from django import forms
from django.forms import SelectMultiple, TextInput, Textarea, ModelForm
from courses.models import Course

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            "title": "Course Title",
            "desc": "Course Description",
            "imageUrl": "Course Image",
            "slug": "Course Slug"
        }
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "desc": Textarea(attrs={"class": "form-control"}),
            "imageUrl": TextInput(attrs={"class": "form-control"}),
            "slug": TextInput(attrs={"class": "form-control"}),
            "categories": SelectMultiple(attrs={"class": "form-control"})
        }
        error_messages = {
            "title": {
                "required":"Please enter the title", 
                "max_length":"You should enter max 50 characters"
            },
            "desc": {
                "required":"Description cannot be left blank"
            }, 
            "imageUrl": {
                "required":"Image url cannot be left blank"
            }, 
            "slug": {
                "required":"Slug cannot be left blank"
            }
        }


