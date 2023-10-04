# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import ct_scan_nodule_1, Mandatory_questionaire_fg, History

User = get_user_model()

@receiver(post_save, sender=ct_scan_nodule_1)
# @receiver(post_save, sender=protocol_deviations)
@receiver(post_save, sender=Mandatory_questionaire_fg)
def track_changes(sender, instance, created, **kwargs):
    if not created:
        # Get the current user, if available
        user = kwargs.get('user', None)
        # If the user is not available in the signal's arguments, try accessing the user from the instance (replace 'user' with the actual attribute name used in your model)
        if user is None and hasattr(instance, 'user'):
            user = instance.user

        if user is not None:
            history = History(
                user=user,
                content_type=ContentType.objects.get_for_model(instance),
                object_id=instance.id,
                field_name='__all__',  # or specify a specific field name here
                old_value='__previous_value__',  # provide the previous value here
                new_value=str(instance),  # convert the instance to a string or provide any other meaningful representation
            )
            print('saved history')
            history.save()
    print('not saved history')
