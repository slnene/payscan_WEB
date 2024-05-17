from .models import PayscanUser,Transaction,Business

from django.contrib import admin

admin.site.register(PayscanUser),
admin.site.register(Business),
admin.site.register(Transaction),
