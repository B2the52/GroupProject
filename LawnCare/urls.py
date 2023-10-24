from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('service_list/', views.ServiceListView.as_view(), name='service_list'),
    path('service_detail/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    path('service/create/', views.ServiceCreate.as_view(), name='service_create')

]