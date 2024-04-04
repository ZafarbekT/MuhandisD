from django.urls import path
from .views import homePage, AllNewsView, OneNewsView, AllProjectsView, OneProjectView, OneStudentView, AllStudentsView

urlpatterns = [
    path('', homePage, name="home"),
    path('allNews', AllNewsView.as_view(), name="allNews"),
    path('newsDetail/<int:pk>/', OneNewsView.as_view(), name='oneNewsDetail'),
    path('allProjects', AllProjectsView.as_view(), name='allProjects'),
    path('projectDetail/<int:pk>/', OneProjectView.as_view(), name='oneProjectDetail'),
    path('allStudents', AllStudentsView.as_view(), name="allStudents"),
    path('studentDetail/<int:pk>/', OneStudentView.as_view(), name="oneStudentDetail"),
]