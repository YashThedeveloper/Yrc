from django.contrib import admin

# Register your models here.
from .models import Contact,Orders, OrderUpdate
admin.site.site_header = 'Yash Road Carriers'
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)