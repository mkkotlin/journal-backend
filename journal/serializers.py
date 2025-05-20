from rest_framework import serializers
from journal.models import JournalEntry, Entry


class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
        read_only_fields = ['user']