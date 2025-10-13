from django.db import models
import re

class ShowManager(models.Manager):
    def basic_validator(self, post):
        errors = {}
        date_pattern = re.compile(r'^(?:(?:19|20)\d\d)-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$')
        if(post['title'] == ""):
            errors['title'] = "you must fill the title"
        
        elif (len(post['title']) < 2):
            errors['title'] = "title must have at least 2 characters"
        
        if(post['network'] == ""):
            errors['network'] = "you must fill the network"
        
        elif (len(post['network']) < 3):
            errors['network'] = "network must have at least 3 characters"
        
        if (post['desc'] == ''):
            errors['dec'] = "you must fill the date"
        
        elif (not date_pattern.match(post['date'])):
            errors['date'] = "date does not match"
        
        if (post['desc'] == ''):
            errors['desc'] = "you must fill the description"
        
        elif (len(post['desc']) < 10):
            errors['network'] = "description must have at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __str__(self):
        return self.title

def all_shows():
    return Show.objects.all()

def update_title(id, title):
    data = Show.objects.get(id = id)
    data.title = title
    data.save()

def update_network(id, net):
    data = Show.objects.get(id = id)
    data.network = net
    data.save()

def update_release_date(id, date):
    data = Show.objects.get(id = id)
    data.release_date = date
    data.save()

def update_description(id, desc):
    data = Show.objects.get(id = id)
    data.description = desc
    data.save()

def remove(id):
    data = Show.objects.get(id = id)
    data.delete()

def get_show(id):
    return Show.objects.get(id = id)

def add_show(context):
    show = Show.objects.create(title = context['title'], network = context['network'], release_date = context['date'], description = context['desc'])
    return show