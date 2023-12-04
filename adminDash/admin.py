from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CorrectUserVotes




class CorrectUserVotesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["user"]}),
        ("CorrectVotes", {"fields": ["correctVotesNumber"]}),
        ("Placement",{"fields": ["currentPlacement"]}),
        ("Student?",{"fields": ["isStudent"]}),
    ]

    ordering = ('currentPlacement','correctVotesNumber')
    list_filter = ["isStudent" ]
    list_display = ["displayName", "currentPlacement","correctVotesNumber", ]









# Register your models here.
admin.site.register(CorrectUserVotes, CorrectUserVotesAdmin)

