from django.urls import path
from .views import UserRegistrationView, UserDetailsView, ReferralsView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('details/', UserDetailsView.as_view(), name='user-details'),
    path('referrals/', ReferralsView.as_view(), name='user-referrals'),
]