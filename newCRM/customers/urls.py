from django.urls import path
from .views import (CustomerListView, CustomerCreateView, CustomerDetailView, CustomerUpdateView, CustomerDeleteView)

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customers-list'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customers-detail'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='customers-update'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customers-delete'),
    path('create/', CustomerCreateView.as_view(), name='customers-create'),

]