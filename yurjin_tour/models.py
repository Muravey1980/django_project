from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.city_name
    

class Airport(models.Model):
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)
    iata_code = models.CharField(max_length=3)
    airport_name = models.CharField(max_length=200)
    #airport_city = models.CharField(max_length=200)
    
    def __str__(self):
        return self.airport_name
    

class Office(models.Model):
    office_name = models.CharField(max_length=200)
    office_adddress = models.CharField(max_length=200)

    def __str__(self):
        return self.office_name
    
    
class Manager(models.Model):
    manager_office = models.ForeignKey(Office, blank=True, null=True, on_delete=models.SET_NULL)
    manager_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.manager_name


class Tourist(models.Model):
    tourist_last_name = models.CharField(max_length=200)
    tourist_first_name = models.CharField(max_length=200)
    tourist_mid_name = models.CharField(max_length=200)
    tourist_passport = models.CharField(max_length=200)
    tourist_international_name = models.CharField(max_length=200)
    tourist_international_passport = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.tourist_last_name + ' ' + self.tourist_first_name + ' ' + self.tourist_mid_name
    
    
class Status(models.Model):
    status_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.status_name

class Contract(models.Model):
    contract_num = models.IntegerField()
    input_date = models.DateField(blank=True, null=True)
    manager = models.ForeignKey(Manager, models.SET_NULL, blank=True, null=True)
    office = models.ForeignKey(Office, models.SET_NULL, blank=True, null=True)
    client = models.ForeignKey(Tourist, models.SET_NULL, blank=True, null=True)
    airport_from1 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_from1', blank=True, null=True)
    airport_to1 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_to1', blank=True, null=True)
    airport_from2 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_from2', blank=True, null=True)
    airport_to2 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_to2', blank=True, null=True)
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)
    conclusion_date = models.DateField()
    signatory = models.ForeignKey(Manager, models.SET_NULL, related_name='contract_signatory', blank=True, null=True)
    tourist_list = models.ManyToManyField(Tourist, related_name='tourist_list') 
    
    
    def __str__(self):
        return 'Договор №' + str(self.contract_num) + ' от ' + str(self.input_date) + ' - ' + self.client.tourist_last_name

    