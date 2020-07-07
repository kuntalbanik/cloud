# from django.contrib.auth.models import User
# from django.db.models import signals
# from django.dispatch import receiver

# from orbit.models import Account, Contact, BillAddress, ShipAddress, Order, OrderFile
# from .models import History, create

# def create_object(receiver, sender):
#     signals.post_save.connect(receiver=create, sender=History)
    # if created:
    #     Account.objects.create(user=instance)

from django.dispatch import Signal
# 
# object_viewed_signal = Signal(providing_args=['instance', 'request'])
