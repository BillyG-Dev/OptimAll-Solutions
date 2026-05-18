from django.db import models

# Create your models here.

class DeploymentBrief(models.Model):
    SERVICE_CHOICES = [
        ('software', 'Software & Mobile App Engineering'),
        ('automation', 'AI Solutions & Business Automation'),
        ('cloud', 'Cloud Deployment & Infrastructure'),
        ('consulting', 'Strategic IT Consultancy'),
        ('other', 'Comprehensive Ecosystem Overhaul'),
        ('portfolio', 'Portfolio Creation, Review & Optimization'),
        ('other', 'Other - Please Specify in Message')
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_display()}"
