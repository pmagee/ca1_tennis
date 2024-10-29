from django.contrib import admin
from .models import TennisClub, Member,Competition

# Register your models here.
admin.site.register(TennisClub)
admin.site.register(Member)
admin.site.register(Competition)