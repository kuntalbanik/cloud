from django.db.models import signals
import datetime

from .models import History

def object_receiver(sender, instance, *args, **kwargs):
    # print("Signal Received")
    pass

def create(app_name, user_name, data, content_type, action_type):
    obj = History(user=user_name, app_label=app_name, object_data=data, content_type=content_type, action_type=action_type)
    obj.save()
    # if object_receiver:
    #     print(object_receiver)
    # else:
    #     pass
    # print("In Model : " +app_name, user_id, data, datetime.datetime.now())
