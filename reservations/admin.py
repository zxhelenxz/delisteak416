from django.contrib import admin

# Register your models here.
from reservations.models import Reserve

admin.site.register(Reserve)