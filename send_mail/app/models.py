from django.db import models
# Create your models here.

class ReplyMail(models.Model):
    id = models.AutoField(primary_key=True)
    sender_email = models.CharField(max_length = 180)
    email = models.CharField(max_length = 180)
    recieve_name = models.CharField(max_length = 180)
    message = models.CharField(max_length=600)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    
    def __str__(self):
        return self.task