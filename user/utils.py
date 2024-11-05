from .models import Customer
def check_email(email):
    if Customer.objects.filter(email=email, type='Normal').exists():
        return True #means already email associated with another account
    else:
        return False 
    
def check_phone(phone):
    if Customer.objects.filter(phone=phone, type='Normal').exists():
        return True #means already email associated with another account
    else:
        return False 
        
def check_email_in_normal(email):
    if Customer.objects.filter(email=email, type='Google').exists():
        return True #means already email associated with another account
    else:
        return False 
    
from django.db.models import Q
from menu.models import TblRedeemedProduct
def check_points_availability(customer, api_points, order):
    customer_points = customer.total_points
    existing_redeemedproducts = TblRedeemedProduct.objects.filter(~Q(state='Completed'), customer=customer, order=order)

    total_poinsForexistingredeemedproducts = 0
    for item in existing_redeemedproducts:
        total_poinsForexistingredeemedproducts += item.redeemproduct.points
    total_redeemedproductsPointsin_tbl = total_poinsForexistingredeemedproducts + api_points
    if total_redeemedproductsPointsin_tbl <= customer_points:
        flag = True
    else:
        flag = False

    return flag

def get_customer_points_after_redeemed(customer, redeemed_points):

    current_points = customer.total_points
    new_points = current_points - redeemed_points

    return new_points
    