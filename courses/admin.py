from django.contrib import admin
from .models import Course
from .models import Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "isActive", "slug","category_list",)
    readonly_fields = ("slug",)
    list_editable = ("isActive",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",),}

    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "course_count",)
    prepopulated_fields = {"slug": ("name",),}

    def course_count(self, obj):
        return obj.course_set.count()