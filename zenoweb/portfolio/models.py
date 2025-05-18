from django.db import models

class Media(models.Model):
    """
    Model to store media files (images, videos, etc.) uploaded by users.
    """
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media {self.id} - {self.file.name}"
    
class Client(models.Model):
    """
    Model to store clients information.
    """

    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    service = models.CharField(max_length=50)
    service_date = models.DateField(blank=True)
    project_details = models.TextField(blank=True)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, Service - {self.service}"
    
    def __repr__(self):
        return f"{self.name}, Service - {self.service}"
