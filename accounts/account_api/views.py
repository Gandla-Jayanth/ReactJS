from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import UserProfile, Referral
from .serializers import UserProfileSerializer, ReferralSerializer

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetailsView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReferralsView(generics.ListAPIView):
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_profile = self.request.user.userprofile
        return Referral.objects.filter(referring_user=user_profile)
