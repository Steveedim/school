from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Classes"
        ordering = ['name']

    def __str__(self):
        return self.name

class Student(models.Model):
    session = models.ForeignKey(Class, related_name='students', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='students', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
