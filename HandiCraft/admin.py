from django.contrib import admin

# Register your models here.
from .models import Sweater,Sock,Scarf,Earring,Vase

admin.site.register(Sweater)
admin.site.register(Sock)
admin.site.register(Scarf)
admin.site.register(Earring)
admin.site.register(Vase)
