from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Referral(models.Model):
    referring_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='referred_by')
    timestamp = models.DateTimeField(auto_now_add=True)