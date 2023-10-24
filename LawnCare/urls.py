from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('service_list/', views.ServiceListView.as_view(), name='service_list'),
    path('service_detail/<int:pk>', views.ServiceDetailView.as_view(), name='book_detail'),

]