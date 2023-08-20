from django.contrib import admin

# Register your models here.
from users.models import Users
from products.admin import BasketAdmin


@admin.register(Users)
class UsersModel(admin.ModelAdmin):
    inlines = (BasketAdmin,)
