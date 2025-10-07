from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"dojo name: {Dojo.name}, city: {Dojo.city}, state: {Dojo.state}"


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"ninja name: {Ninja.first_name} {Ninja.last_name}"


def add_dojo(context):
    Dojo.objects.create(name=context['name'], city=context['city'], state=context['state'])

def add_ninja(ninja):
    Ninja.objects.create(first_name = ninja['fname'], last_name = ninja['lname'], dojo = ninja['dojo'])

def get_dojo(dojo_id):
    return Dojo.objects.get(id = dojo_id)

def get_all_dojos():
    return Dojo.objects.all()

def get_all_ninjas():
    return Ninja.objects.all()
