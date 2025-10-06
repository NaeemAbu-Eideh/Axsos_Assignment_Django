from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_all_records():
        return User.objects.all()
    
    def create_record(data):
        User.objects.create(fname=data['fname'], lname=data['lname'], email=data['email'], age=data['age'])
