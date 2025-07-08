from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Notes
from .utils import get_category
@receiver(pre_save,sender=Notes)
def add_category(sender,instance,**kwargs):
    instance.category=get_category(instance.title,instance.description)
