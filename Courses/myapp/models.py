from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, post):
        errors = {}
        if(post['title'] == ""):
            errors['title'] = "Name field is empty, fill it"
        
        elif(len(post['title']) < 5):
            errors['title'] = "Name should have at least 5 characters"
        
        if(post['desc'] == ""):
            errors['desc'] = "Description is empty, fill it"
        
        elif(len(post['desc']) < 10):
            errors['desc'] = "Description should have at least 10 characters"
        
        return errors

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

def get_all_courses():
    return Course.objects.all()

def get_course(id):
    return Course.objects.get(id = id)

def delete_course(id):
    course = Course.objects.get(id = id)
    course.delete()

def add_course(post):
    return Course.objects.create(title = post['title'], description = post['desc'])