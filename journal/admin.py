from django.contrib import admin
from journal.models import Entry, JournalEntry

# Register your models here.
admin.site.register(Entry)
admin.site.register(JournalEntry)