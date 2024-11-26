from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.username, email=instance.email)

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
@receiver(post_save, sender=User)
def move_profile_picture(sender, instance, created, **kwargs):
    if instance.profile_picture:
        # Tentukan path file lama dan tujuan
        old_path = instance.profile_picture.path
        new_path = os.path.join(settings.STATIC_ROOT, 'images', os.path.basename(old_path))

        # Pindahkan file ke folder static/images/
        shutil.move(old_path, new_path)

        # Set path baru untuk file image yang sudah dipindahkan
        instance.profile_picture.name = os.path.join('images', os.path.basename(new_path))
        instance.save()