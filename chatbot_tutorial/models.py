from django.db import models

class ButtonUsage(models.Model):

    User = models.AutoField(primary_key=True)

    stupidButton = models.IntegerField()

    fatButton = models.IntegerField()

    dumbButton = models.IntegerField()
