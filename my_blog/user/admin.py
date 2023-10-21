from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (None, { "fields": ('username','password')}),
        ('Redes Sociales',{'fields':('web_site',)})
        
    )
    


# Register your models here.
