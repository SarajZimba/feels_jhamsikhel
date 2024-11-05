import datetime
import random
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from alice_menu.utils import BaseModel
from datetime import datetime
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Customer(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=True, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=False)
    type = models.CharField(max_length=255, null=True, blank=False)
    cardNo = models.CharField(max_length=255, null=True, blank=False)
    vatNo = models.CharField(max_length=255, null=True, blank=False)
    # dob = models.CharField(max_length=100, null=True, blank=False)
    loyalty_points = models.FloatField(default=0.0)
    dob = models.DateField(null=True, blank=True)
    review_points = models.FloatField(default=0.0)
    total_points = models.FloatField(default=0.0)
    
    def joined_since(self):
        # Calculate the difference between now and the created_at field
        if self.created_at:
            now_date = now()
            delta = relativedelta(now_date, self.created_at)
            years = delta.years
            months = delta.months
            days = delta.days

            # Create a human-readable string
            parts = []
            if years > 0:
                parts.append(f"{years} year{'s' if years > 1 else ''}")
            if months > 0:
                parts.append(f"{months} month{'s' if months > 1 else ''}")
            if days > 0:
                parts.append(f"{days} day{'s' if days > 1 else ''}")

            return ', '.join(parts) if parts else 'Less than a day'
        else:
            return 'No creation date available'

    def __str__(self):
        return f"{self.name} - ({self.email})"

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = f"{self.username}@silverlinepos.com"
        self.total_points = self.loyalty_points + self.review_points
        self.total_points = round(self.total_points, 2)
        self.loyalty_points = round(self.loyalty_points, 2)
        self.review_points = round(self.review_points, 2)
        super().save(*args, **kwargs)

class CustomerNormalLoginManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        
        user = self.model(username=username, **extra_fields)
        if password is not None:
            user.set_password(password)
        user.save(using=self._db)
        return user
    
class CustomerNormalLogin(AbstractBaseUser):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    email = models.CharField(max_length=255, null=True)
    reset_token = models.CharField(max_length = 1000, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=255, null=True)
    reset_token_expiry = models.DateTimeField(null=True, blank=True)

    objects = CustomerNormalLoginManager()

    def __str__(self):
        return self.username
    
# class CustomerGooglelogin(BaseModel):
#     customer = models.ForeignKey(Customer, models.SET_NULL, null=True)
#     email = models.CharField(max_length=255, null=True)
#     google_id = models.CharField(max_length=200, null=True)
#     def __str__(self):
#         return f"{self.customer.name}"

class CustomerGoogleLoginManager(BaseUserManager):
    def create_user(self, username, google_id=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        
        user = self.model(username=username, **extra_fields)
        if google_id is not None:
            user.set_password(google_id)
        user.save(using=self._db)
        return user

class CustomerGoogleLogin(AbstractBaseUser):
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True)
    email = models.CharField(max_length=255, null=True)
    google_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f"{self.customer.name}"
    
class UserLogin(BaseModel):
    device_token = models.CharField(max_length=355)
    outlet = models.CharField(max_length=100)



import datetime
import random
import uuid

from django.contrib.auth.models import AbstractUser

from django.db import models




class User(AbstractBaseUser, BaseModel):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to="user/images/", null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - ({self.email})"

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = f"{self.username}@silverlinepos.com"
        super().save(*args, **kwargs)