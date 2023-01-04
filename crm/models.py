from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)