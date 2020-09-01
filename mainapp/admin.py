from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class UserOneCInline(admin.StackedInline):
    model = UserOneC
    can_delete = False
    verbose_name_plural = 'Создать пользователя 1С'
    fk_name = 'user'

class UserAdmin(UserAdmin):
    inlines = (UserOneCInline, )


# class MultiFormOneCAdmin(admin.StackedInline):
#     model = MultiFormOneC

# @admin.register(FormToOneC)
# class FormToOneCAdmin(admin.ModelAdmin):
#     inlines = [MultiFormOneCAdmin]

#     class Meta:
#        model = FormToOneC

# @admin.register(MultiFormOneC)
# class MultiFormOneCAdmin(admin.ModelAdmin):
#     pass
 

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserOneC)
admin.site.register(FormToOneC)
