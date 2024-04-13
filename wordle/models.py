from django.db import models
import django

# Create your models here.

class mang(models.Model):
    oige_sona = models.CharField(max_length=200)
    mitmes = models.IntegerField(default=1)
    arvatud = models.BooleanField(default=False)
    mang_labi = models.BooleanField(default=False)
    sona1 = models.JSONField(default=list(("", "", "", "", "")))
    sona1_varv = models.JSONField(default=list(("white", "white", "white", "white", "white")))
    sona2 = models.JSONField(default=list(("", "", "", "", "")))
    sona2_varv = models.JSONField(default=list(("white", "white", "white", "white", "white")))
    sona3 = models.JSONField(default=list(("", "", "", "", "")))
    sona3_varv = models.JSONField(default=list(("white", "white", "white", "white", "white")))
    sona4 = models.JSONField(default=list(("", "", "", "", "")))
    sona4_varv = models.JSONField(default=list(("white", "white", "white", "white", "white")))
    sona5 = models.JSONField(default=list(("", "", "", "", "")))
    sona5_varv = models.JSONField(default=list(("white", "white", "white", "white", "white")))
    def __str__(self):
        return str(self.mitmes)+"\n"+self.oige_sona+"\nid: "+str(self.id)