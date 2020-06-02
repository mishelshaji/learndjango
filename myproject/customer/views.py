from django.shortcuts import render, HttpResponse
from .forms import *
from .models import Orders, Customer

# Create your views here.
def home(request):
    # mform = MOrderForm()
    # return render(request, 'customer_home.html', {'form': mform})
    # order = Orders()
    # order.product = "some product"
    # order.price = 50
    # order.customer = Customer.objects.get(pk=3)
    # order.save()

    # order = Orders.objects.get(pk=2)
    # customer = Customer.objects.get(pk=order.customer_id)
    # return HttpResponse(customer.email)
    # data = Orders.objects.filter(customer__email="staff@gmail.com")

    # request.session["data"] = "some message"
    # return HttpResponse(request.session["data"])
    if request.method == "GET":
        orderform = OrderForm()
        return render(request, 'customer_home.html', {'data': orderform})
    
    else:
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            order = Orders()
            order.product = orderform.cleaned_data["product"]
            order.price = orderform.cleaned_data["price"]
            order.customer = Customer.objects.get(pk=orderform.cleaned_data["customer"])
            order.save()
            return HttpResponse("Saved")
        else:
            return render(request, 'customer_home.html', {'data': orderform})