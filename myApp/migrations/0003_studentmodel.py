# Generated by Django 5.0.3 on 2024-03-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_projectsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_fullname', models.CharField(max_length=50)),
                ('student_bio', models.CharField(max_length=200)),
                ('student_telegram', models.CharField(max_length=150)),
                ('student_facebook', models.CharField(max_length=150)),
                ('student_instagram', models.CharField(max_length=150)),
                ('student_photo', models.ImageField(upload_to='students/')),
            ],
        ),
    ]
