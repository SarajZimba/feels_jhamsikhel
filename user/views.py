from django.shortcuts import render
from django.contrib.auth import get_user_model, logout
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy("user:login_view"))


from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from alice_menu.utils import DeleteMixin
from .models import Customer
from .forms import CustomerForm
from user.permission import IsAdminMixin, AdminBillingMixin

class CustomerMixin(AdminBillingMixin):
    model = Customer
    form_class = CustomerForm
    paginate_by = 50
    queryset = Customer.objects.filter(status=True, is_deleted=False)
    success_url = reverse_lazy("user:customer_list")
    search_lookup_fields = ["name","phone", "email"]


class CustomerList(CustomerMixin, ListView):
    template_name = "customer/customer_list.html"
    queryset = Customer.objects.active()


class CustomerDetail(CustomerMixin, DetailView):
    template_name = "customer/customer_detail.html"


class CustomerCreate(CustomerMixin, CreateView):
    template_name = "create.html"


class CustomerUpdate(CustomerMixin, UpdateView):
    template_name = "update.html"


class CustomerDelete(CustomerMixin, DeleteMixin, View):
    pass