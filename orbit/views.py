from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.db.models import signals, Q
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group

import csv
from datetime import datetime, timedelta


# from django.contrib.contenttypes.models import ContentType
# from django.contrib.admin.models import LogEntry, ADDITION
# import re

from .models import OrderAccount, Industry, Account, Contact, State, Order, OrderFile, BillAddress, ShipAddress
from account.models import User
from .apps import OrbitConfig
from history.mixins import object_receiver, create
from history.models import History
# from history.mixins import ObjectViewMixin
# from history.mixins import create, object_viewed_receiver

from .forms import AccountForm, ContactForm, OrderForm, BillAddressForm, ShipAddressForm
# 
# CONSTANTS
app_name = OrbitConfig.name
#
# 
# 
# 
# Signal Function
def signal_ready(receiver, sender):
    signals.post_save.connect(receiver=receiver, sender=sender)



# Basic views
# Index page view
def index(request):
    # return HttpResponse("<h2>Hello ORBIT</h2>")
    # return render(request, 'auth/login.html')
    return redirect('/home/')


# Home / Landing Page view
@login_required
def home(request):
    uname = request.user.username
    order = Order.objects.all().filter(order_booking_status=1) |\
            Order.objects.all().filter(advance_status=1) |\
            Order.objects.all().filter(balance_status=1) |\
            Order.objects.all().filter(delivery_status=1) |\
            Order.objects.all().filter(commissioning_status=1) |\
            Order.objects.all().filter(commission_status=1)
    data = History.objects.all().filter(user=uname)
    context = {'data' : data, 'order' : order}
    return render(request, 'home.html', context)


@login_required
def recent_actions(request):
    uname = request.user.username
    data = History.objects.all().filter(user=uname)
    context = {'data' : data}
    return render(request, 'orbit/recent_actions.html', context)


@login_required
def pending_tasks(request):
    order = Order.objects.all().filter(order_booking_status=1) |\
            Order.objects.all().filter(advance_status=1) |\
            Order.objects.all().filter(balance_status=1) |\
            Order.objects.all().filter(delivery_status=1) |\
            Order.objects.all().filter(commissioning_status=1) |\
            Order.objects.all().filter(commission_status=1)
    context = {'order' : order}
    return render(request, 'orbit/pending_tasks.html', context)


@login_required
def search_link(request):
    if request.method == "POST":
        data = request.POST.get("search")
        if len(data) < 3:
            context = {'data' : data }
        else:
            # For Accounts
            account = Account.objects.all().filter(name__icontains=data)
            # For Orders 
            order = Order.objects.all().filter(order_no__icontains=data) | \
                    Order.objects.all().filter(so_no__icontains=data) | \
                    Order.objects.all().filter(account__name__icontains=data)
            # For Contacts
            contact = Contact.objects.all().filter(account__name__icontains=data) | \
                    Contact.objects.all().filter(contact_name__icontains=data) | \
                    Contact.objects.all().filter(contact_no__icontains=data)
            # 
            # Reserved context data
            context = {'data' : data, 'account' : account, 'contact' : contact, 'order' : order }
    return render(request, 'orbit/results.html', context)


# Account Create view
@user_passes_test(lambda u: Group.objects.get(name='accounts') in u.groups.all())
def accountAdd(request):
    # Using Signal example
    # signals.post_save.connect(receiver=object_receiver, sender=Account)
    # 'created': True, 'update_fields': None,
    user_name = request.user.username
    content_type = 'Account'
    action_type = 'Create'
    # 
    signal_ready(object_receiver, Account)
    # 
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        create(app_name, user_name, request.POST['name'], content_type, action_type)
        return HttpResponseRedirect('/orders/create/')
    return render(request, "orbit/account.html", {"form" : form,})


# Account List view (Class Based)
class AccountList(LoginRequiredMixin, ListView):
    model = Account


# Account Details View
@login_required
def accountdetails(request, pk):
    account = get_object_or_404(Account, pk=pk)
    contacts = Contact.objects.all().filter(account_id=pk)
    billAddress = BillAddress.objects.all().filter(account_id=pk)
    shipAddress = ShipAddress.objects.all().filter(account_id=pk)
    orders = Order.objects.all().filter(account_id=pk)
    context = {'contacts': contacts, 'account': account, 'billAddress': billAddress, 'shipAddress': shipAddress, 'orders': orders}
    return render(request, 'orbit/account_detail.html', context)


# Contact Create View
@user_passes_test(lambda u: Group.objects.get(name='accounts') in u.groups.all())
def contactAdd(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect("/orders/create/")
    return render(request, "orbit/contact_form.html", {"form" : form,})


# Contact Update view
@method_decorator(user_passes_test(lambda u: Group.objects.get(name='accounts') in u.groups.all()),
name='dispatch')
class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['contact_name', 'contact_no', 'email', 'job_title']



# Order Create View with Group permission of 'accounts'
@user_passes_test(lambda u: Group.objects.get(name='accounts') in u.groups.all())
def OrderCreate(request):
    user_name = request.user.username
    content_type = 'Order'
    action_type = 'Create'
    # 
    signal_ready(object_receiver, Order)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        create(app_name, user_name, request.POST['order_no'], content_type, action_type)
        return HttpResponseRedirect("/orders/")
    return render(request, "orbit/order_form.html", {"form" : form,})


# Order List view
class OrderList(LoginRequiredMixin, ListView):
    model = Order


# Order Details View
@login_required
def orderdetails(request, pk):
    order = get_object_or_404(Order, pk=pk)
    orderFile = OrderFile.objects.all().filter(order_id=pk).values()
    context = {'order': order, 'orderFile': orderFile}
    return render(request, 'orbit/order_detail.html', context)


# Order Update view with Group permission of 'accounts'
@method_decorator(user_passes_test(lambda u: Group.objects.get(name='accounts') in u.groups.all()),
name='dispatch')
class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    def form_valid(self, form):
        content_type = 'Order'
        action_type = 'Update'
        user_name = self.request.user.username
        signal_ready(object_receiver, Order)
        post = form.save(commit=False)
        # print(post.pk)
        post.save()
        create(app_name, user_name, self.request.POST['order_no'], content_type, action_type)
        # print(user_name)
        return redirect('/orders/'+str(post.pk)+'/')

    fields = ['order_status', 'order_type', 'category', 'order_no', 'order_date', 'product_description', 
            'uom', 'qty', 'amount', 'tax', 'division', 'order_booking_status', 'so_no', 'payment_terms', 
            'advance_amount', 'advance_status', 'balance_amount', 'balance_status', 'delivery_date', 
            'supervision_scope', 'transporter', 'freight_terms', 'local_purchase_required', 
            'local_purchase_required_date', 'di_status', 'di_date', 'delivery_status', 'commissioning_status', 
            'commissioning_amount', 'commission_status', 'commission_amount', 'sales_person', 'remarks']


# Billing Address Create view
@user_passes_test(lambda u: Group.objects.get(name='accounts') in u.groups.all())
def BillingAddressCreate(request):
    form = BillAddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/orders/create/")
	
    return render(request, "orbit/address.html", {"form" : form})


# Shipping Address Create view
@user_passes_test(lambda u: Group.objects.get(name='accounts') in u.groups.all())
def ShippingAddressCreate(request):
    form = ShipAddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/orders/create/")
	
    return render(request, "orbit/address.html", {"form" : form})


class OrderFileCreate(LoginRequiredMixin, CreateView):
    model = OrderFile
    fields = ['order', 'title', 'file']


# Order related files Update view
class OrderFileUpdate(LoginRequiredMixin, UpdateView):
    model = OrderFile
    fields = ['order','title', 'file']

# ========================================
# Reports Section
# ========================================
@user_passes_test(lambda u: Group.objects.get(name='division') in u.groups.all())
def reports(request, pk=None, date1=None, date2=None):
    N_DAY = 366
    N_DAY_HALF = 183
    orderAccount = OrderAccount.objects.all()
    order=''
    # response = ''
    # 
    if pk==None:
        # print("No data")
        # 
        # 
        if request.method == "POST":
            if request.POST.get("date1") and request.POST.get("date2"):
                d1 = request.POST.get("date1")
                d2 = request.POST.get("date2")
                # 
                dt1 = str(d1).split('-')
                year1 = int(dt1[0])
                month1 = int(dt1[1])
                day1 = int(dt1[2])
                date1 = datetime(year1,month1,day1)
                # print(year1, month1, day1)
                # 
                dt2 = str(d2).split('-')
                year2 = int(dt2[0])
                month2 = int(dt2[1])
                day2 = int(dt2[2])
                date2 = datetime(year2,month2,day2)
                # print(year2, month2, day2)
                diff = date2 - date1

                if diff.days <= N_DAY:
                    order = Order.objects.filter(order_date__range=[d1, d2])
                    print(diff.days)
                # else:
                #     print(diff.days)
        # 
    else:
        # 
        today = datetime.now()
        today1 = str(today.date())
        # 
        today_6_M = today - timedelta(days=N_DAY_HALF)
        today_6 = str(today_6_M.date())
        # 
        order = Order.objects.filter(order_date__range=[today_6, today1]) &\
                Order.objects.all().filter(order_account_id=pk)
        # 
    context = {'order': order, 'orderAccount': orderAccount }
    return render(request, "orbit/reports.html", context)

# 
# 
# # Export to csv
# def csvExport(request):
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="reports.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#     writer.writerow(['Second row', 'A', 'B', 'C'])

#     return response