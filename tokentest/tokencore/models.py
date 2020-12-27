import random
import string
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='user')

    referral_code = models.CharField(max_length=50)
    referred_by = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='referred_by')

    email_verified = models.BooleanField()
    mobile_phone_verified = models.BooleanField()

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=10)
    email = models.EmailField(default='1@gmail.com')

    created_at = models.DateField()
    last_login = models.DateField()

    def create_referral_code(self, size):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()