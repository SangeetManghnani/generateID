from django.db import models
from django.utils import timezone

class Information(models.Model) :
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=50, null=True)
    address = models.TextField(null=True)
    published_date = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.first_name

