from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    address = models.CharField(max_length=124)
    address_2 = models.CharField(max_length=124, default='', blank=True)
    city = models.CharField(max_length=124)
    country = models.CharField(max_length=124)
    postal_code = models.CharField(max_length=64)


class User(AbstractUser):
    pass


#     created_at = models.DateTimeField(auto_now_add=True)
#     is_coach = models.BooleanField(default=False)
#     is_client = models.BooleanField(default=False)
#     is_med = models.BooleanField(default=False)
#
#     def get_client_profile(self):
#         client_profile = None
#         if hasattr(self, 'clientprofile'):
#             client_profile = self.clientprofile
#         return client_profile
#
#     def get_med_profile(self):
#         med_profile = None
#         if hasattr(self, 'medprofile'):
#             med_profile = self.medprofile
#         return med_profile
#
#     def get_coach_profile(self):
#         coach_profile = None
#         if hasattr(self, 'coachprofile'):
#             client_profile = self.coachprofile
#         return coach_profile
#
#
class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    @property
    def get_name(self):
        return self.user.username


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class MedProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
