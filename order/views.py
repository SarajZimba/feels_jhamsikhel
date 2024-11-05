from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomeView(self):
    return HttpResponse("It is working")



from django.urls import reverse_lazy
from .models import HashValue
# from .forms import QrForm
# from .forms import OrganizationForm
from user.permission import IsAdminMixin, SearchMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    View,
    TemplateView,

)

from alice_menu.utils import DeleteMixin
from django.shortcuts import render


class QrMixin(IsAdminMixin):
    model = HashValue
    paginate_by = 50    
    queryset = HashValue.objects.all()
    success_url = reverse_lazy("qr_list")
    # search_lookup_fields = [
    #     "title",
    #     "menutype__title",
    # ]


class QrList(QrMixin, ListView):
    template_name = "qr/qr-list.html"
    queryset = HashValue.objects.all()


class QrDetail(QrMixin, DetailView):
    template_name = "qr/qr-list.html"


# class MenuTypeCreate(MenuTypeMixin, CreateView):
#     template_name = "create.html"


# class MenuTypeUpdate(MenuTypeMixin, UpdateView):
#     template_name = "update.html"


# class MenuTypeDelete(MenuTypeMixin, DeleteMixin, View):
#     pass