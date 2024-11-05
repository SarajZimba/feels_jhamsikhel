from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    logout_user,
)


app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login_view"),
    path("logout/", logout_user, name="logout"),
]


from .views import (
    CustomerList,
    CustomerDetail,
    CustomerCreate,
    CustomerUpdate,
    CustomerDelete,
)

urlpatterns += [
    path("customer/", CustomerList.as_view(), name="customer_list"),
    path("customer/<int:pk>/", CustomerDetail.as_view(), name="customer_detail"),
    path("customer/create/", CustomerCreate.as_view(), name="customer_create"),
    path("customer/<int:pk>/update/", CustomerUpdate.as_view(), name="customer_update"),
    path("customer/delete", CustomerDelete.as_view(), name="customer_delete"),
]
