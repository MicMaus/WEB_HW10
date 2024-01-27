from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


@receiver(post_save, sender=User)
def assign_staff_status(sender, instance, created, **kwargs):
    if created:
        # Assign staff status to the newly created user
        instance.is_staff = True
        instance.save()

        # Add permission to add Author
        add_author_perm = Permission.objects.get(codename="add_author")
        add_quote_perm = Permission.objects.get(codename="add_quote")
        instance.user_permissions.add(add_author_perm)
        instance.user_permissions.add(add_quote_perm)
