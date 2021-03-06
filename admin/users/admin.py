from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Permission, Role
from django.utils.translation import gettext_lazy as _


class UserAppAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'role')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('date_joined', 'last_login',)
    search_fields = ('username',)
    list_filter = ('username',)


admin.site.register(User, UserAppAdmin)
admin.site.register(Permission)
admin.site.register(Role)

