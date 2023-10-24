from django.shortcuts import render
from .models import Service, Review, RequestContact, UserReview, Invoice
from django.views import generic
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


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


class ServiceCreate(CreateView):
    model = Service
    fields = ['service_id', 'service_title', 'service_info', 'service_cost']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('author_list'))