from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100, blank=True,null=True)
    department_description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)

    def _str_(self):
        return self.department_name



class Roles(models.Model):
    role_name = models.CharField(max_length=100, blank=True,null=True)
    role_description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)
    

