import random

from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from carrier.models import Customer
from .forms import CustomerModelForm
from .mixins import OrganisorAndLoginRequiredMixin


class CustomerListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "customers/customer_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Customer.objects.filter(organisation=organisation)


class CustomerCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "customers/customer_create.html"
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse("customers:customers-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_customer = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Customer.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to be an customers",
            message="You were added as an customers on crm. Please come login to start working.",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        return super(CustomerCreateView, self).form_valid(form)


class CustomerDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "customers/customer_detail.html"
    context_object_name = "customers"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Customer.objects.filter(organisation=organisation)


class CustomerUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "customers/customer_update.html"
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse("customers:customers-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Customer.objects.filter(organisation=organisation)


class CustomerDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "customers/customer_delete.html"
    context_object_name = "customers"

    def get_success_url(self):
        return reverse("customers:customers-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Customer.objects.filter(organisation=organisation)
