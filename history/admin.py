from django.contrib import admin
from .models import History
# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user','app_label','object_data','content_type','action_type','action_time')
admin.site.register(History, HistoryAdmin)