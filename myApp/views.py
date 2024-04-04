from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsModel, ProjectsModel, StudentModel


def homePage(request):
    news = NewsModel.objects.all()[:3]
    projects = ProjectsModel.objects.all()[:3]
    students = StudentModel.objects.all()[:4]
    context = {
        'news': news,
        'projects': projects,
        'students': students
    }
    return render(request, 'home.html', context)

class AllNewsView(ListView):
    model = NewsModel
    template_name = 'allNews.html'

class OneNewsView(DetailView):
    model = NewsModel
    template_name = 'oneNews.html'

class AllProjectsView(ListView):
    model = ProjectsModel
    template_name = 'allProjects.html'

class OneProjectView(DetailView):
    model = ProjectsModel
    template_name = 'oneProject.html'

class AllStudentsView(ListView):
    model = StudentModel
    template_name = 'allStudents.html'

class OneStudentView(DetailView):
    model = StudentModel
    template_name = 'oneStudent.html'
