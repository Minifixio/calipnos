from django.db import models

# Create your models here.

class DeviceMeasure(models.Model):
    id = models.AutoField(primary_key=True)
    config_id = models.IntegerField(default=None, blank=True, null=True)
    version = models.IntegerField()
    config = models.JSONField()
    pta = models.JSONField()
    upload_date = models.DateTimeField(auto_now_add=True)
    points_count = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class DeviceMeasurePoint(models.Model):
    measure = models.ForeignKey(DeviceMeasure, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    battery = models.FloatField()
    integrity = models.FloatField()
    sp02 = models.FloatField()
    bpm = models.FloatField()
    obda = models.FloatField()
    audio_sp1 = models.FloatField()
    audio_sp2 = models.FloatField()
    audio_sp3 = models.FloatField()
    audio_sp4 = models.FloatField()
    audio_sp5 = models.FloatField()
    audio_sp6 = models.FloatField()
    audio_sp7 = models.FloatField()
    audio_sp8 = models.FloatField()
    audio_sp9 = models.FloatField()
    audio_sp10 = models.FloatField()