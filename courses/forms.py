from django import forms
from django.forms import SelectMultiple, TextInput, Textarea, ModelForm, Form, ImageField
from courses.models import Course
from PIL import Image

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            "title": "Course Title",
            "desc": "Course Description",
            "image": "Course Image",
            "slug": "Course Slug"
        }
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "desc": Textarea(attrs={"class": "form-control"}),
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
            "image": {
                "required":"Image cannot be left blank"
            }, 
            "slug": {
                "required":"Slug cannot be left blank"
            }
        }


class UploadForm(Form):
    image = ImageField()