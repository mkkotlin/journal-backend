from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from journal.models import JournalEntry, Entry
from journal.serializers import JournalEntrySerializer, EntrySerializer, UserRegisterSerializer
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
    serializer_class = JournalEntrySerializer

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

class  EntryDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class JournalUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalEntrySerializer

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

class EntryUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)