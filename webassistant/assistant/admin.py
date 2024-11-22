from django.contrib import admin

from django.contrib import admin
from reg.models import CustomUser
from django.contrib.auth.admin import UserAdmin


from django.contrib import admin
from reg.models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Указываем отображаемые поля
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

    # Какие поля можно редактировать
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')
                }),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_permissions')}),  # Убираем 'groups'
    )

    # Переопределяем видимую форму при создании нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('collapse',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )
    ordering = ('username',)

# Регистрируем модель
admin.site.register(CustomUser, CustomUserAdmin)