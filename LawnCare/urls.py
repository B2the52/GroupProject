from django.urls import path, re_path, include
from . import views
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('service_list/', views.ServiceListView.as_view(), name='service_list'),
    path('service_detail/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    path('service/create/', views.ServiceCreate.as_view(), name='service_create'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('accounts/', include('django.contrib.auth.urls')),


]