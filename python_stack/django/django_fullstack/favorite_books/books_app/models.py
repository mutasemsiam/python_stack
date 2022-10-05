from django.db import models
from login_app.models import User

class BookManager(models.Manager):
    def book_validator(self, posted_data):
        errors = {}
        
        if len(posted_data['desc']) < 5:
            errors['desc_lenth'] = "Description must be at least 5 characters!"
        
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_books", on_delete = models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
