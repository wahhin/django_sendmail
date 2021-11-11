from django.db import models

# Create your models here.
class feargreed(models.Model):
    Daily_Fear_Greed = models.DateField(max_length=200)
    Fear_Greed = models.DecimalField(max_digits=25, decimal_places=20)
    class Meta:
        db_table = 'feargreed'

class nyse(models.Model):
    Daily_NYSE = models.DateField(max_length=200)
    NYSE_Up_Vol = models.DecimalField(max_digits=25, decimal_places=20)
    class Meta:
        db_table = 'nyse'

class riskapp(models.Model):
    Daily_Riskapp = models.DateField(max_length=200)
    Risk_App = models.DecimalField(max_digits=25, decimal_places=20)
    class Meta:
        db_table = 'riskapp'

class bullratio(models.Model):
    Weekly_Bull = models.DateField(max_length=200)
    Bull_ratio = models.DecimalField(max_digits=25, decimal_places=20)
    class Meta:
        db_table = 'bullratio'

class putcall(models.Model):
    Daily_putcall = models.DateField(max_length=200)
    Put_Call = models.DecimalField(max_digits=25, decimal_places=20)
    class Meta:
        db_table = 'putcall'


class Screenshot(models.Model):
    screenshot = models.ImageField(upload_to='img/screenshots/', help_text='Html2canvas screenshot')