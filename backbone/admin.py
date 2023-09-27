from django.contrib import admin
from .models import Student
from .translation import StudentTranslationOptions
from modeltranslation.admin import TranslationAdmin


class StudentAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name", "surname")}
    list_display = ('name', 'surname')


admin.site.register(Student, StudentAdmin)
