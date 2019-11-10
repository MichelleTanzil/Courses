from __future__ import unicode_literals
from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be at least 5 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=60)
    comment = models.TextField(blank = True)
    description = models.OneToOneField('Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __repr__(self):
        return f"<Course Object: {self.id} {self.name}>"


class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['description']) < 15:
            errors["description"] = "The description for the course should be at least 15 characters"
        return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DescriptionManager()

    def __repr__(self):
        return f"<Description Object: {self.id} {self.content} >"

