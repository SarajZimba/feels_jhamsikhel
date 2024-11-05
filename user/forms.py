from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from alice_menu.forms import BaseForm

from .models import Customer


class CustomerForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured",
            "created_by",
            "email",
        ]
