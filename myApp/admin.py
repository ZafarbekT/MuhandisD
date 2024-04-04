from django.contrib import admin
from .models import NewsModel, ProjectsModel, StudentModel

admin.site.register(NewsModel)

admin.site.register(ProjectsModel)

admin.site.register(StudentModel)
