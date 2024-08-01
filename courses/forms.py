from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(label="Course Title", required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    desc = forms.CharField(label="Course Description", widget=forms.Textarea(attrs={"class":"form-control"}))
    imageUrl = forms.CharField(label="Course Image", widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.SlugField(label="Course Slug",widget=forms.TextInput(attrs={"class":"form-control"}))