from django.contrib import admin
from django.urls import  path
from .views import (
    TestAuthView, JournalEntryListview, EntryListView, 
    JournalDeleteView, EntryDeleteView, UserRegisterView,
    JournalUpdateView, EntryUpdateView
)

urlpatterns = [
    path('test/', TestAuthView.as_view()),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('journals/', JournalEntryListview.as_view(), name='journal_list'),
    path('entry/', EntryListView.as_view(), name='entry'),
    path('journals/<int:pk>/', JournalDeleteView.as_view(), name='delete_list'),
    path('entry/<int:pk>/', EntryDeleteView.as_view(), name='entry-delete'),
    path('journals/<int:pk>/update/', JournalUpdateView.as_view(), name='journal_update'),
    path('entry/<int:pk>/update/', EntryUpdateView.as_view(), name='entry_update'),
]