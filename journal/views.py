from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from journal.models import JournalEntry, Entry
from journal.serializers import JournalEntrySerializer, EntrySerializer
from rest_framework import status, generics

# Create your views here.

class TestAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"user":request.user.username})
    

class JournalEntryListview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        journals = JournalEntry.objects.filter(user = request.user).order_by('-created_at')
        serializer = JournalEntrySerializer(journals, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = JournalEntrySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EntryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        enties = Entry.objects.filter(user=self.request.user).order_by('-date')
        serializer = EntrySerializer(enties, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = EntrySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user, is_private=True)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class  JournalDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class  EntryDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer