from django.contrib import admin
from users.models import VerifyCode


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', "add_time"]
