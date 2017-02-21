from django.contrib import admin

from .models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "descp", "admin", "status")

admin.site.register(Block, BlockAdmin)