from django.shortcuts import render
from .models import Service, Review, RequestContact, UserReview, Invoice
from django.views import generic


# Create your views here.
def index(request):
    num_services = Service.objects.all().count()
    context = {
        'num_services': num_services
    }
    return render(request, 'index.html', context=context)


class ServiceListView(generic.ListView):
    model = Service


class ServiceDetailView(generic.DetailView):
    model = Service


def about_us(request):
    num_services = Service.objects.all().count()
    context = {
        'num_services': num_services
    }
    return render(request, 'about_us.html', context=context)


def blog(request):
    num_services = Service.objects.all().count()
    context = {
        'num_services': num_services
    }
    return render(request, 'blog.html', context=context)