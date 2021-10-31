from django.urls import path
from .views import (
    CarrierListView, CarrierDetailView, CarrierCreateView, CarrierUpdateView, CarrierDeleteView,
    AssignCustomerView, CategoryListView, CategoryDetailView, CarrierCategoryUpdateView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CarrierJsonView,
    FollowUpCreateView, FollowUpUpdateView, FollowUpDeleteView
)

app_name = "carriers"

urlpatterns = [
    path('', CarrierListView.as_view(), name='carrier-list'),
    path('json/', CarrierJsonView.as_view(), name='carrier-list-json'),
    path('<int:pk>/', CarrierDetailView.as_view(), name='carrier-detail'),
    path('<int:pk>/update/', CarrierUpdateView.as_view(), name='carrier-update'),
    path('<int:pk>/delete/', CarrierDeleteView.as_view(), name='carrier-delete'),
    path('<int:pk>/assign-customer/', AssignCustomerView.as_view(), name='assign-customer'),
    path('<int:pk>/category/', CarrierCategoryUpdateView.as_view(), name='carrier-category-update'),
    path('<int:pk>/followups/create/', FollowUpCreateView.as_view(), name='carrier-followup-create'),
    path('followups/<int:pk>/', FollowUpUpdateView.as_view(), name='carrier-followup-update'),
    path('followups/<int:pk>/delete/', FollowUpDeleteView.as_view(), name='carrier-followup-delete'),
    path('create/', CarrierCreateView.as_view(), name='carrier-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
]