from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(CoachProfile)
admin.site.register(ClientProfile)
admin.site.register(MedProfile)
