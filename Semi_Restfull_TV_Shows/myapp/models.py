from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
    data.title = net
    data.save()

def update_release_date(id, date):
    data = Show.objects.get(id = id)
    data.title = date
    data.save()

def update_description(id, desc):
    data = Show.objects.get(id = id)
    data.title = desc
    data.save()

def remove(id):
    data = Show.objects.get(id = id)
    data.delete()

def get_show(id):
    return Show.objects.get(id = id)

def add_show(context):
    show = Show.objects.create(title = context['title'], network = context['network'], release_date = context['date'], description = context['desc'])
    return show