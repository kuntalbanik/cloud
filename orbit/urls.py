"""cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views, auth

urlpatterns = [
    # 
    # 
    # Basic views
    path('', views.index, name = 'index'),
    path('login/', auth.login, name = 'login'),
    path('logout/', auth.logout, name = 'logout'),
    path('home/', views.home, name = 'home'),
    path('actions/', views.recent_actions, name = 'actions'),
    path('pending/', views.pending_tasks, name = 'pending_tasks'),
    path('search/', views.search_link, name = 'search'),
    # path('register/', auth.register, name = 'register'),
    # 
    #     
    # Custom View Paths
    # Account related views
    path('account/create/', views.accountAdd, name = 'account_create'),
    path('account/', views.AccountList.as_view(), name = 'account_list'),
    path('account/<int:pk>/', views.accountdetails, name = 'account_detail'),
    # 
    # 
    # Order Related Views
    path('orders/', views.OrderList.as_view(), name = 'orders_list'),
#     path('orders/<int:pk>/', views.OrderDetail.as_view(), name = 'orders_detail'),
    path('orders/<int:pk>/', views.orderdetails, name = 'orders_detail'),
    path('orders/create/', views.OrderCreate, name = 'order_create'),
    path('orders/update/<int:pk>/', views.OrderUpdate.as_view(), name = 'orders_update'),
    # path('orders/create/', views.OrderCreate.as_view(), name = 'order_create'),
    # 
    # 
    # Address related views
    path('billaddress/create/', views.BillingAddressCreate, name = 'billaddr_create'),
    path('shipaddress/create/', views.ShippingAddressCreate, name = 'shipaddr_create'),

    # path('contact/create/', views.ContactCreate.as_view(), name = 'contact_create'),
    path('contact/create/', views.contactAdd, name = 'contact_create'),
    path('contact/update/<int:pk>/', views.ContactUpdate.as_view(), name = 'contact_update'),
    # 
    #
    # Order File related views
    path('ordersfile/create/', views.OrderFileCreate.as_view(), name = 'orderfiles_create'),
    path('ordersfile/update/<int:pk>/', views.OrderFileUpdate.as_view(), name = 'orderfiles_update'),
    # path('ordersfile/create/', views.createOrderFiles, name = 'orderfiles_create'),
    # path('ordersfile/update/<int:pk>/', views.createOrderFiles, name = 'orderfiles_update'),
#     path('ordersfile/<int:pk>/', views.OrderFileDetail.as_view(), name = 'orderfiles_detail'),
#     path('ordersfile/<int:pk>/', views.orderfiles, name = 'orderfiles_detail'),
    # path('sessions/delete/(?P<pk>[0-9]+)/$', views.SessionDelete.as_view(), name = 'sessions_delete'),
#     path('submit/$', views.submit_session, name = 'submit_session'),
    # 
    # 
    # Reports links
    path('reports/', views.reports, name = 'reports'),
    path('reports/<int:pk>/', views.reports, name = 'reports_detail'),
    # csv export
    # path('export/', views.csvExport, name = 'export'),
]




# pathpatterns = [
# 	path('', include('orbit.paths')),
# ]