from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=90)
    load_from = models.CharField(max_length=30, default="")
    truck_number = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=111)
    unload_in = models.CharField(max_length=30, default="")
    about_product = models.CharField(max_length=111, default="")

    def __int__(self):
        return self.order_id

class OrderUpdate(models.Model):
    order_id = models.CharField(max_length=25, default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:20] + "..."