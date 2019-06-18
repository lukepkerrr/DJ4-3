from django.contrib import admin

# Register your models here.
from .models import Phone, Apple, Samsung, Xiaomi

class PhoneAdm(admin.ModelAdmin):
    pass

class AppleAdm(admin.ModelAdmin):
    pass

class SamsungAdm(admin.ModelAdmin):
    pass

class XiaomiAdm(admin.ModelAdmin):
    pass

admin.site.register(Phone, PhoneAdm)
admin.site.register(Apple, AppleAdm)
admin.site.register(Samsung, SamsungAdm)
admin.site.register(Xiaomi, XiaomiAdm)