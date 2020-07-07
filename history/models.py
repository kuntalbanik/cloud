from django.db import models



# Create your models here.
# Historical Record storage
# 
# Model User History
class History(models.Model):
    user = models.CharField(max_length=30)
    app_label = models.CharField(max_length=30)
    object_data = models.CharField(max_length=250)
    content_type = models.CharField(max_length=30)
    action_type = models.CharField(max_length=30)
    action_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.app_label)+" - "+str(self.object_data)

    class Meta:
        verbose_name_plural = "Histories"



