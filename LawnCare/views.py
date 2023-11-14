from django.shortcuts import render
from .models import Service, Review, RequestContact, UserReview, Invoice, BlogPost
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
    return render(request, 'LawnCare/index.html', context=context)


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
    fields = ['serv_id', 'serv_title', 'serv_info', 'serv_cost']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('service_list'))


class ReviewCreate(CreateView):
    model = Review
    fields = ['rev_rating', 'rev_comments', 'serv_id']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('service_list'))


class BlogCreate(CreateView):
    model = BlogPost
    fields = ['Blog_title', 'Blog_text']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('blog'))


class BlogDetailView(generic.DetailView):
    model = BlogPost


class BlogListView(generic.ListView):
    model = BlogPost
