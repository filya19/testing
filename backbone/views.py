from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Student


# Create your views here.

def index(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about us.html")


def kraty(request):
    students = Student.objects.all()
    return render(request, "kraty.html", {'student_list': students})


def kraty_detail(request, kraty_slug):
    student_detail = get_object_or_404(Student, slug=kraty_slug)
    return render(request, 'kraty_detail.html', {'student': student_detail})


def radio(request):
    if request.method == "POST":
        lang = request.POST['lang']
    else:
        return HttpResponse('Failed')
