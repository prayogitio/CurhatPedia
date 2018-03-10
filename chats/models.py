from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user_one = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING, related_name='user_one')
    user_two = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING, related_name='user_two')
    message = models.TextField()

    def __unicode__(self):
        return self.message