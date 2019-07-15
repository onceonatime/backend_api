from django.contrib import admin

# Register your models here.
from .models import Datas
from .models import ByTime

admin.site.register(Datas)
admin.site.register(ByTime)