
# from .models import File

# class FileForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = ('file', )
# from django import forms

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

'''
Created on Aug 4, 2019

@author: kuntal
'''
from django.forms import ModelForm
from django import forms
from .models import Account, Contact, Order, OrderFile, BillAddress, ShipAddress
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = ['title', 'abstract', 'track', 'speaker']
#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args, **kwargs)
#         # self.helper = FormHelper()
#         # self.helper.form_class = 'form-horizontal'
#         # self.helper.label_class = 'col-md-offset-1 col-md-2'
#         # self.helper.field_class = 'col-md-8'
#         # self.helper.add_input(Submit('submit', 'Submit'))


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'name', 'industry', 'pan', 'ph_no'
        ]


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['account', 'contact_name', 'contact_no', 'email', 'job_title']


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = [
			'order_account', 'account', 'contact', 'billing_address', 'shipping_address', 'order_type', 'category', 
            'order_no', 'order_date', 'product_description', 'uom', 'qty', 'amount', 'tax', 'division', 
            'order_status', 'order_booking_status', 'so_no', 'payment_terms', 'advance_amount', 
            'advance_status', 'balance_amount', 'balance_status', 'delivery_date', 'supervision_scope', 
            'transporter', 'freight_terms', 'local_purchase_required', 'local_purchase_required_date', 
            'di_status', 'di_date', 'delivery_status', 'commissioning_status', 'commissioning_amount', 
            'commission_status', 'commission_amount', 'sales_person', 'remarks'
		]

class BillAddressForm(forms.ModelForm):
	class Meta:
		model = BillAddress
		fields = [
			'account', 'address_type', 'address', 'city', 'dist',
            'state', 'pin', 'gst']


class ShipAddressForm(forms.ModelForm):
	class Meta:
		model = ShipAddress
		fields = [
			'account', 'address_type', 'address', 'city', 'dist',
            'state', 'pin', 'gst']