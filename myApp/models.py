from django.db import models

class NewsModel(models.Model):
    news_theme = models.CharField(max_length=200)
    short_description = models.TextField()
    full_description = models.TextField()
    news_photo = models.ImageField(upload_to='news/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_theme
    
class ProjectsModel(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_photo = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.project_name
    
class StudentModel(models.Model):
    student_fullname = models.CharField(max_length=50)
    student_bio = models.CharField(max_length=200)
    student_photo = models.ImageField(upload_to='students/')
    student_link1 = models.CharField(max_length=150, blank=True)
    student_link2 = models.CharField(max_length=150)
    student_link3 = models.CharField(max_length=150)
    student_link4 = models.CharField(max_length=150)

    def __str__(self):
        return self.student_fullname
