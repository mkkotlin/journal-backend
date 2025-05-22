from django.contrib import admin
from django.urls import  path
from .views import TestAuthView, JournalEntryListview, EntryListView, JournalDeleteView, EntryDeleteView

urlpatterns = [
    path('test/', TestAuthView.as_view()),
    path('journals/', JournalEntryListview.as_view(), name='journal_list'),
    path('entry/', EntryListView.as_view(), name='entry'),
    path('journals/<int:pk>/', JournalDeleteView.as_view(), name='delete_list'),
    path('entry/<int:pk>/',EntryDeleteView.as_view(), name = 'entry-delete')
]