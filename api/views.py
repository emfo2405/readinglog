from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book, Review, ReadingStatus
from .serializers import BookSerializer, ReviewSerializer, ReadingStatusSerializer, UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .permissions import IsOwner

# View för Book
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# View för Review
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Koppla review till user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View för Readingstatus
class ReadingStatusViewSet(ModelViewSet):
    queryset = ReadingStatus.objects.all()
    serializer_class = ReadingStatusSerializer
    permission_classes = [IsAuthenticated]

    # Koppla readingstatus till user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View för en lista av Users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# View för att registrera en användare
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# View för att visa eller uppdatera sin profil
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        return self.request.user