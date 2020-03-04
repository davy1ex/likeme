from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Likerer


class LikererInline(admin.StackedInline):
    model = Likerer
    can_delete = False
    verbose_name_plural = 'likerer'


class UserAdmin(BaseUserAdmin):
    inlines = (LikererInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
