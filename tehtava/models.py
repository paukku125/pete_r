from django.db import models

# Create your models here.
# MUISTA lisätä admin.py tiedostoon myös

class Antiqua(models.Model):
    orderNumber = models.IntegerField(null=True)
    personName = models.CharField(max_length=200, null=True)
    healtCare = models.CharField(max_length=200, null=True)
    injections = models.CharField(max_length=200, null=True)
    arrived = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.personName

class SolarBuddhica(models.Model):
    orderNumber = models.IntegerField(null=True)
    personName = models.CharField(max_length=200, null=True)
    healtCare = models.CharField(max_length=200, null=True)
    injections = models.CharField(max_length=200, null=True)
    arrived = models.CharField(max_length=200, null=True)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return self.personName

class Vaccinations(models.Model):
    gender = models.CharField(max_length=200, null=True)
    vaccinationDate = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.gender

class Zerpfy(models.Model):
    orderNumber = models.IntegerField(null=True)
    personName = models.CharField(max_length=200, null=True)
    healtCare = models.CharField(max_length=200, null=True)
    injections = models.CharField(max_length=200, null=True)
    arrived = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.personName

    