from django.contrib import admin
from .models import DateEntry, choice


class choiceInline(admin.StackedInline):
    model = choice
    extra = 3

class DateEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Valid on", {"fields": ["start_date", "end_date"]}),
        ("Video",{"fields": ["videoLink"]}),
    ]
    inlines = [choiceInline]




# Register your models here.
admin.site.register(DateEntry, DateEntryAdmin)
admin.site.register(choice)