from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name','email', 'is_staff', 'is_active',)
    list_filter = ('first_name','email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password',
            )
            }
        ),
        ('Personal information', {
            'fields': (
                'first_name', 'last_name',
            )
            }
        ),
        ('Permissions', {'fields': ('token', 'is_staff', 'is_active','groups')}),
        ('Activity', {
            'fields': (
                'last_login','date_joined',
            )
            }
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'email', 'password1', 'password2', 'is_staff',
                'is_active', 'groups'
            )
            }
        ),
    )
    readonly_fields = ('last_login','date_joined',)
    search_fields = ('email',)
    ordering = ('first_name',)

admin.site.register(CustomUser, CustomUserAdmin)
