# from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
# from django.shortcuts import redirect
# from account.models import User
from .validators import validate_file_size, validate_file_extension

# from . import forms
# Create your models here.
# 
# 
# 
# Order Account Model
class OrderAccount(models.Model):
    orderAccount = models.CharField(max_length=50)

    def __str__(self):
        return self.orderAccount


# 
# Industry Model
class Industry(models.Model):
    industry = models.CharField(max_length=60)

    def __str__(self):
        return self.industry



# Accounts Model
class Account(models.Model):
    name = models.CharField(max_length=120, unique=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING)
    pan = models.CharField(max_length=10, blank=True)
    # contacts = models.ManyToManyField('Contacts', models.CASCADE)
    # bill_addr = models.ManyToManyField('Address', models.CASCADE)
    # ship_addr = models.ManyToManyField('Address', models.CASCADE)
    ph_no = models.CharField(max_length=14)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Files Account Model
class AccountFile(models.Model):
    account = models.ForeignKey(Account, models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)+" - "+str(self.account)


# Contact Model
class Contact(models.Model):
    account = models.ForeignKey(Account, models.CASCADE)
    contact_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=14)
    email = models.CharField(max_length=30)
    job_title = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account) +" - "+ self.contact_name +", "+self.contact_no

    def get_absolute_url(self):
        # return redirect('orders_detail', pk=self.order)
        return reverse('account_detail', kwargs={'pk':self.account_id})



#Address Type Model
class AddressType(models.Model):
    address_type = models.CharField(max_length=12, help_text='Address Type [ Billing / Shipping ]')

    def __str__(self):
        return self.address_type


# State Model
class State(models.Model):
    state = models.CharField(max_length=30, help_text='Indian State')

    def __str__(self):
        return self.state


# Billing Address Model
class BillAddress(models.Model):
    account = models.ForeignKey(Account, models.CASCADE)
    address_type = models.ForeignKey(AddressType, models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=20)
    dist = models.CharField(max_length=20)
    state = models.ForeignKey(State, models.CASCADE)
    pin = models.CharField(max_length=8)
    gst = models.CharField(max_length=15)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account)+ " - "+  self.address +', '+ self.city +', ' + self.dist +', ' + str(self.state) + ', '+ self.pin


# Shipping Address Model
class ShipAddress(models.Model):
    account = models.ForeignKey(Account, models.CASCADE)
    address_type = models.ForeignKey(AddressType, models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=20)
    dist = models.CharField(max_length=20)
    state = models.ForeignKey(State, models.CASCADE)
    pin = models.CharField(max_length=8)
    gst = models.CharField(max_length=15)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account)+ " - "+  self.address +', '+ self.city +', ' + self.dist +', ' + str(self.state) + ', '+ self.pin


# Individual options model
# Order Type Model
class OrderType(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type


# Order Category Model
class OrderCategory(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.category


# UOM Model
class ProductUOM(models.Model):
    uomProduct =  models.CharField(max_length=12)

    def __str__(self):
        return self.uomProduct


# Tax Model
class IndiaTax(models.Model):
    tax_rate = models.CharField(max_length=30)

    def __str__(self):
        return self.tax_rate


# Order booking status Model
class OrderBookingStatus(models.Model):
    order_booking_status = models.CharField(max_length=12)

    def __str__(self):
        return self.order_booking_status
    

# Advance Status Model
class AdvanceStatus(models.Model):
    advance_status = models.CharField(max_length=12)

    def __str__(self):
        return self.advance_status


# Balance Status Model
class BalanceStatus(models.Model):
    balance_status = models.CharField(max_length=12)

    def __str__(self):
        return self.balance_status
    

# Supervision Model
class Supervision(models.Model):
    supervision_scope = models.CharField(max_length=80)

    def __str__(self):
        return self.supervision_scope
    

# Delivery Status Model
class DeliveryStatus(models.Model):
    delivery_status = models.CharField(max_length=20)

    def __str__(self):
        return self.delivery_status


# Commissioning Status Model
class CommissioningStatus(models.Model):
    commissioning_status = models.CharField(max_length=12)

    def __str__(self):
        return self.commissioning_status
    

# Commission Status Model
class CommissionStatus(models.Model):
    commission_status = models.CharField(max_length=12)

    def __str__(self):
        return self.commission_status
        

# Division Model
class Division(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# OrderStatus Model
class OrderStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# ####################################
# NEW ADDED

# Freight Terms Model
class FreightTerms(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# DI Status Model
class DiStatus(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Transporter Model
class Transporter(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

# Local Purchase Model
class LocalPurchase(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Sales person Model
class SalesPerson(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


# Orders Model
class Order(models.Model):
    order_account = models.ForeignKey(OrderAccount, models.CASCADE)
    account = models.ForeignKey(Account, models.CASCADE)
    contact = models.ForeignKey(Contact, models.CASCADE)
    billing_address = models.ForeignKey(BillAddress, models.CASCADE)
    shipping_address = models.ForeignKey(ShipAddress, models.CASCADE)
    order_type = models.ForeignKey(OrderType, models.CASCADE)
    category = models.ForeignKey(OrderCategory, models.CASCADE)
    order_no = models.CharField(max_length=45, unique=True)
    order_date = models.DateField(auto_now=False)
    product_description = models.CharField(max_length=255, help_text='[ Enter brief description about product ]')
    uom = models.ForeignKey(ProductUOM, models.CASCADE)
    qty = models.IntegerField()
    amount = models.FloatField()
    tax = models.ForeignKey(IndiaTax, models.CASCADE)
    division = models.ForeignKey(Division, models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, models.CASCADE)
    order_booking_status = models.ForeignKey(OrderBookingStatus, models.CASCADE)
    so_no = models.CharField(max_length=40, help_text='[ SO Number from Principal Company ]', null=True, blank=True)
    payment_terms = models.CharField(max_length=255)
    advance_amount = models.FloatField()
    advance_status = models.ForeignKey(AdvanceStatus, models.CASCADE, help_text='[ ABG / Advance Recived? ]')
    balance_amount = models.FloatField()
    balance_status = models.ForeignKey(BalanceStatus, models.CASCADE, help_text='[ PBG / Balance Received? ]')
    delivery_date = models.DateField(auto_now=False)
    supervision_scope = models.ForeignKey(Supervision, models.CASCADE, help_text='[ Supervision / E&C Scope ]')
    transporter = models.ForeignKey(Transporter, models.CASCADE, null=True, blank=True)
    freight_terms = models.ForeignKey(FreightTerms, models.CASCADE, null=True, blank=True)
    local_purchase_required = models.ForeignKey(LocalPurchase, models.CASCADE)
    local_purchase_required_date = models.DateField(auto_now=False, null=True, blank=True)
    # -----------------------------------------------
    di_status = models.ForeignKey(DiStatus, models.CASCADE, null=True, blank=True)
    di_date = models.DateField(auto_now=False, null=True, blank=True)
    delivery_status = models.ForeignKey(DeliveryStatus, models.CASCADE)
    commissioning_status = models.ForeignKey(CommissioningStatus, models.CASCADE)
    commissioning_amount = models.FloatField(help_text='[ Pending payments for site commissioning ]', null=True, blank=True)
    commission_status = models.ForeignKey(CommissionStatus, models.CASCADE)
    commission_amount = models.FloatField(help_text='[ Commision are yet to receive from Principal Company for this order ]', null=True, blank=True)
    sales_person = models.ForeignKey(SalesPerson, models.CASCADE, null=True, blank=True)
    remarks = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_no +" - "+ str(self.account)

    def get_absolute_url(self):
        return reverse('orders_detail', kwargs={'pk':self.pk})



# Order attachment Model
class OrderFileAttachment(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Files Order Model
class OrderFile(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    title = models.ForeignKey(OrderFileAttachment, models.CASCADE)
    # file = forms.FileFieldForm()
    file = models.FileField(validators=[validate_file_extension, validate_file_size ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)+" - "+str(self.order)
    
    def get_absolute_url(self):
        # return redirect('orders_detail', pk=self.order)
        return reverse('orders_detail', kwargs={'pk':self.order_id})
        # return reverse('orders_detail', kwargs={'pk':self.pk})
    # def get_success_url(self):
    #     # return reverse('index')
    #     return reverse('orders_detail', kwargs={'pk':self.pk})