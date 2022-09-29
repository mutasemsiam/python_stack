from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def new_validator(self, posted_data):
        errors = {}
        for show in Show.objects.all():
            if show.title == posted_data['title']:
                errors['duplicate_title'] = "Show already exists!"
                return errors
        if len(posted_data['title']) < 2:
            errors['title_lenth'] = "Title must be at least 2 characters!"
        
        if len(posted_data['network']) < 3:
            errors['network'] = "Network must be at least 3 characters!"

        if len(posted_data['desc']) and len(posted_data['desc']) < 10:
            errors['desc'] = "Description must be at least 10 characters!"

        if posted_data['release_date'] and posted_data['release_date'] > str(datetime.now()):
            errors['release_date'] = "Date must be in the past!"

        # if str(posted_data['title']).isalpha() == False:
        #     errors['title_char'] = "Title must contain characters only!"

        return errors

    def edit_validator(self, posted_data, show_id):
        errors = {}
        for show in Show.objects.exclude(id = show_id):
            if show.title == posted_data['title']:
                errors['duplicate_title'] = "Show already exists!"
                return errors
        if len(posted_data['title']) < 2:
            errors['title_lenth'] = "Title must be at least 2 characters!"
        
        if len(posted_data['network']) < 3:
            errors['network'] = "Network must be at least 3 characters!"

        if len(posted_data['desc']) and len(posted_data['desc']) < 10:
            errors['desc'] = "Description must be at least 10 characters!"

        if posted_data['release_date'] and posted_data['release_date'] > str(datetime.now()):
            errors['release_date'] = "Date must be in the past!"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


