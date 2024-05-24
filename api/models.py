from django.db import models


class SessionData(models.Model):
    CaptureTime = models.CharField(max_length=12, null=True, blank=True)
    SessionEndedAt = models.CharField(max_length=12, null=True, blank=True)
    SessionStartedAt = models.CharField(max_length=12, null=True, blank=True)
    Session_for = models.CharField(max_length=255, default='')
    arousal = models.FloatField(null=True, blank=True)
    attention = models.FloatField(null=True, blank=True)
    dominantEmotion = models.CharField(max_length=50, null=True, blank=True, default='Neutral')
    userEmail = models.EmailField(max_length=254)
    valence = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    
    def _str_(self):
        return self.userEmail
    


