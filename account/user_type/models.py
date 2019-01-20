# eta all general_user er model

from django.db import models
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
#from generaluser.models import User

# A class for general user (doctor+patient)

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bmdc = models.IntegerField(null=True, blank=True)


class Patient(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    disease = models.TextField(blank=True, null=True)


class Doctor_1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bmdc = models.IntegerField(null=True, blank=True)


class Patient_1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disease = models.TextField(blank=True, null=True)


'''
Todo List:

Patient profile update korte hobe]
Doctor model ready hoy nai

'''


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('**************************************************************************************************************')
        print(instance)
        Profile.objects.create(user=instance)
        instance.profile.save()

        if instance.doctor == 0:
            Patient_1.objects.create(user=instance)
            instance.profile.save()
        else:
            Doctor_1.objects.create(user=instance)
            instance.profile.save()


'''
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
