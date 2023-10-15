from django.contrib import admin
from .models import DateEntry, Choice, Vote


class choiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class DateEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Valid on", {"fields": ["start_date", "end_date"]}),
        ("Video",{"fields": ["videoLink", "resolutionVidLink"]}),
        ("Question",{"fields": ["question"]}),
    ]
    inlines = [choiceInline]






# Register your models here.
admin.site.register(DateEntry, DateEntryAdmin)
admin.site.register(Choice)
admin.site.register(Vote)