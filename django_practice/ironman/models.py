from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    power = models.BooleanField(default=False)
    bio = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True)
    organization = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Equipment(models.Model):
    Site = models.CharField(max_length=20)
    UserSite = models.CharField(max_length=20)
    # ExportSite = models.CharField(max_length=20,null=True)
    # OwnerSite = models.CharField(max_length=20,null=True)
    # SEQ = models.IntegerField(blank=True, null=True)
    EQP_ID = models.CharField(max_length=20, primary_key=True, unique=True)
    User_EQP_ID = models.CharField(max_length=20)
    # Export_EQP_ID = models.CharField(max_length=20,null=True)
    # Owner_EQP_ID = models.CharField(max_length=20,null=True)
    # Mobus_Id = models.CharField(max_length=20,null=True)
    # ComPort_Id = models.IntegerField(blank=True, null=True)
    DESCRIPTION = models.CharField(max_length=200)
    EQP_TYPE = models.CharField(max_length=20)
    EQP_VENDOR = models.CharField(max_length=20)
    # EQP_MODE = models.CharField(max_length=20,null=True)
    # EQP_MODEL = models.CharField(max_length=20,null=True)
    # EQP_OFFSET = models.IntegerField(blank=True, null=True)
    # EQP_WPH = models.FloatField(blank=True, null=True)
    # TIMEZONE = models.CharField(max_length=20,null=True)
    # TCS_OUTPUT_ACTIVE = models.CharField(max_length=20,null=True)
    # TCS_ALARM_ACTIVE = models.CharField(max_length=20,null=True)
    # TCS_TOOLHOURLYMOVE_ACTIVE = models.CharField(max_length=20,null=True)
    # TCS_LOTHOURLYMOVE_ACTIVE = models.CharField(max_length=20,null=True)
    # TCS_DAILYANALYSIS_ACTIVE = models.CharField(max_length=20,null=True)
    # TCS_LOTANALYSIS_ACTIVE = models.CharField(max_length=20,null=True)
    # LM_TIME = models.DateTimeField(null=True)
    # LM_USER = models.CharField(max_length=20,null=True)
    # Language = models.CharField(max_length=50,null=True)
    # SYS_Status = models.CharField(max_length=20,null=True)
    # SYS_DataDeleteDate = models.DateTimeField(null=True)
    # SYS_FileImportTime = models.DateTimeField(null=True)
    # SYS_WarnKWH = models.IntegerField(null=True)
    # SYS_WarnWPH = models.IntegerField(null=True)
    # SYS_WarnESH = models.IntegerField(null=True)
    # SYS_WarnExpire = models.IntegerField(null=True)
    # SYS_WarnCOM = models.IntegerField(null=True)
    # SYS_WarnAlarm = models.IntegerField(null=True)
    # SYS_WarnTracker = models.IntegerField(null=True)
    # SYS_WarnTrackerAlarm = models.IntegerField(null=True)
    # SYS_WarnOther = models.IntegerField(null=True)
    # MAC = models.CharField(max_length=100,null=True)
    # Export_SiteSummary_Date = models.DateTimeField(null=True)

    def __str__(self):
        self.Site

    class Meta:
        managed = False
        db_table = "equipment"
