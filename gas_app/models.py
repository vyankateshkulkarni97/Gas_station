from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)

class Service_Request(models.Model):
    SERVICE_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Meter Installation', 'Meter Installation'),
        ('Bill Inquiry', 'Bill Inquiry'),
    ]

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ])
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    description = models.TextField()
    resolution_date = models.DateTimeField(null=True, blank=True)
    files = models.FileField(upload_to='service_request_files/', null=True, blank=True)

class SupportRepresentative(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

