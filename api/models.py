from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=240)
    created_by = models.ForeignKey(User , related_name='fix_request', on_delete=models.PROTECT)
    fix_by = models.ForeignKey(User,related_name = 'repair_by',on_delete=models.PROTECT)
    description = models.TextField(max_length = 3000,blank=True, null=True)
    is_fixed = models.BooleanField(("Fixed"),default=False)
    
    
    def __str__(self):
        return self.title