from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from journal.models import JournalEntry, Entry
from journal.serializers import JournalEntrySerializer, EntrySerializer

# Create your views here.

class TestAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"message":"Auth True from backend"})
    

class JournalEntryListview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        journals = JournalEntry.objects.filter(user = request.user).order_by('-created_at')
        serializer = JournalEntrySerializer(journals, many=True)
        return Response(serializer.data)
    
class EntryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        enties = Entry.objects.all().order_by('-date')
        serializer = EntrySerializer(enties, many=True)
        return Response(serializer.data)