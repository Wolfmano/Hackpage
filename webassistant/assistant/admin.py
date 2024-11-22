from django.contrib import admin

from .models import Ticket
from .models import Category  # Импортируем модель Category
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


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at')
    search_fields = ('title', 'category__name')  # Позволяет искать тикеты по категориям


# Создаем класс админки для модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Какие поля будут отображаться в списке
    search_fields = ('name',)  # Добавляем поиск по названию категории
    list_filter = ('name',)  # Фильтры по категориям

# Регистрируем модель и админский класс
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(CustomUser, CustomUserAdmin)