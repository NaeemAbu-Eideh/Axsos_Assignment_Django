from django.db import models
import myapp.models as user_models
import re

class MessageManager(models.Manager):
    def basic_validator(self, post):
        errors = {}
        if(post['desc'] == ""):
            errors['desc'] = "Message must not be empty, fill it"
        
        elif (len(post['desc']) < 10 or len(post['desc']) > 500):
            errors['desc'] = "Message length must be between 10 and 500 characters"
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, post):
        errors = {}
        if(post['desc'] == ""):
            errors['desc'] = "Comment must not be empty, fill it"
        
        elif (len(post['desc']) < 10 or len(post['desc']) > 500):
            errors['desc'] = "Comment length must be between 10 and 500 characters"
        return errors

class Message(models.Model):
    message_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ForeignKey(user_models.User, related_name="messages", on_delete=models.CASCADE)
    objects = MessageManager()

class Comment(models.Model):
    comment_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    messages = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    users = models.ForeignKey(user_models.User, related_name="comments", on_delete=models.CASCADE)
    objects = CommentManager()

def add_message(message, user):
    man = user_models.User.objects.get(id = user['id'])
    return Message.objects.create(message_description = message['desc'], users = man)

def get_all_messages():
    return Message.objects.all()

def add_comment(comment, message_id):
    message = Message.objects.get(id = message_id)
    user_id = message.users.id
    user = user_models.User.objects.get(id = user_id)
    Comment.objects.create(comment_description = comment['desc'], messages = message, users = user)
