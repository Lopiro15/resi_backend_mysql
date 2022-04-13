from django.contrib import admin

# Register your modelf

from User.models import *

@admin.register(CustomUser)
class ClientAdmin(admin.ModelAdmin):
    
    list_display = ('username', 'email')
