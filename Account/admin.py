from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

class AccountAdmin(UserAdmin):
    list_display = ('email' , 'username' , 'date_joined' , 'last_login' , 'is_admin' , 'is_staff')
    search_fields = ('email' , 'username')
    readonly_fields = ('id' , 'date_joined' , 'last_login')

    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()

admin.site.register(Customer,AccountAdmin)

