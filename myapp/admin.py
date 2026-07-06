from django.contrib import admin

# Register your models here.
from . models import datas,user
admin.site.register(datas)
admin.site.register(user)
