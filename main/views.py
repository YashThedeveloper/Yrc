from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Orders, OrderUpdate
import json
# Create your views here.


def home(request):
    return render(request, 'index.html')
def tracker(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        about_product = request.POST.get('about_product', '')
        order = Orders( name=name, email=email, about_product=about_product)
        order.save()

        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')
def clients(request):
    return render(request, 'clients.html')
def gallery(request):
    return render(request, 'gallery.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email,phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')
