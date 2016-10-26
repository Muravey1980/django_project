from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=200)


class City(models.Model):
    city_name = models.CharField(max_length=200)
    

class Airport(models.Model):
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)
    iata_code = models.CharField(max_length=3)
    airport_name = models.CharField(max_length=200)
    #airport_city = models.CharField(max_length=200)


class Office(models.Model):
    office_name = models.CharField(max_length=200)

    def __str__(self):
        return self.office_name
    
    
class Manager(models.Model):
    manager_office = models.ForeignKey(Office, blank=True, null=True, on_delete=models.SET_NULL)
    manager_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.manager_name


class Tourist(models.Model):
    tourist_name = models.CharField(max_length=200)
    tourist_passport = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tourist_name
    
    
class Status(models.Model):
    status_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.status_name

class Contract(models.Model):
    contract_num = models.IntegerField
    input_date = models.DateField(blank=True, null=True)
    manager = models.ForeignKey(Manager, blank=True, null=True, on_delete=models.SET_NULL)
    office = models.ForeignKey(Office, blank=True, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Tourist, blank=True, null=True, on_delete=models.SET_NULL)
    airport_from1 = models.ForeignKey(Airport, related_name='airport_from1', blank=True, null=True, on_delete=models.SET_NULL)
    airport_to1 = models.ForeignKey(Airport, related_name='airport_to1', blank=True, null=True, on_delete=models.SET_NULL)
    airport_from2 = models.ForeignKey(Airport, related_name='airport_from2', blank=True, null=True, on_delete=models.SET_NULL)
    airport_to2 = models.ForeignKey(Airport, related_name='airport_to2', blank=True, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL)
    conclusion_date = models.DateField()
    signatory = models.ForeignKey(Manager, related_name='contract_signatory', blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.contract_num) + ' от ' + str(self.input_date)
    