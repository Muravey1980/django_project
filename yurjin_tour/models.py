from django.db import models

# Create your models here.
class Country(models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        
    country_name = models.CharField(max_length=200, verbose_name="Название")
    
    def __str__(self):
        return self.country_name

class City(models.Model):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        
    city_name = models.CharField(max_length=200, verbose_name="Название")
    
    def __str__(self):
        return self.city_name
    

class Airport(models.Model):
    class Meta:
        verbose_name = "Аэропорт"
        verbose_name_plural = "Аэропорты"
        
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Страна")
    iata_code = models.CharField(max_length=3, verbose_name="Код IATA")
    airport_name = models.CharField(max_length=200, verbose_name="Наименование")
    #airport_city = models.CharField(max_length=200)
    
    def __str__(self):
        return self.airport_name
    

class Office(models.Model):
    class Meta:
        verbose_name = "Офис"
        verbose_name_plural = "Офисы"
        
    office_name = models.CharField(max_length=200, verbose_name="Наименование")
    office_adddress = models.CharField(max_length=200, verbose_name="Адрес")

    def __str__(self):
        return self.office_name
    
    
class Manager(models.Model):
    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"
        
    manager_office = models.ForeignKey(Office, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Офис")
    manager_name = models.CharField(max_length=200, verbose_name="ФИО")
    
    def __str__(self):
        return self.manager_name


class Tourist(models.Model):
    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристы"
    
    tourist_last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    tourist_first_name = models.CharField(max_length=200, verbose_name="Имя")
    tourist_mid_name = models.CharField(max_length=200, verbose_name="Отчество")
    tourist_passport = models.CharField(max_length=200, verbose_name="Паспорт РФ")
    tourist_international_passport = models.CharField(max_length=200, verbose_name="Загранпаспорт")
    tourist_international_name = models.CharField(max_length=200, verbose_name="Имя как в загранпаспорте")
    tourist_email = models.EmailField(blank=True, null=True, verbose_name="e-mail")
    
    
    def __str__(self):
        return self.tourist_last_name + ' ' + self.tourist_first_name[0] + '.' + self.tourist_mid_name[0]+'.'
    
    
class Status(models.Model):
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        
    status_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.status_name

class Contract(models.Model):
    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"
        
    contract_num = models.IntegerField(verbose_name="Номер договора")
    input_date = models.DateField(blank=True, null=True, verbose_name="Дата ввода")
    manager = models.ForeignKey(Manager, models.SET_NULL, blank=True, null=True, verbose_name="Менеджер")
    office = models.ForeignKey(Office, models.SET_NULL, blank=True, null=True, verbose_name="Офис")
    client = models.ForeignKey(Tourist, models.SET_NULL, blank=True, null=True, verbose_name="Клиент")
    airport_from1 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_from1', blank=True, null=True, verbose_name="Аэропорт отправления туда")
    airport_to1 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_to1', blank=True, null=True, verbose_name="Аэропорт прибытия туда")
    airport_from2 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_from2', blank=True, null=True, verbose_name="Аэропорт отправления обратно")
    airport_to2 = models.ForeignKey(Airport, models.SET_NULL, related_name='airport_to2', blank=True, null=True, verbose_name="Аэропорт прибытия обратно")
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True, verbose_name="")
    conclusion_date = models.DateField(verbose_name="Дата подписания")
    date_begin = models.DateField(blank=True, null=True, verbose_name="Дата начала")
    date_finish = models.DateField(blank=True, null=True, verbose_name="Дата окончания")
    contract_sum = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True, verbose_name="Сумма контракта")
    prepayment_sum = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True, verbose_name="Сумма предоплаты")
    signatory = models.ForeignKey(Manager, models.SET_NULL, related_name='contract_signatory', blank=True, null=True, verbose_name="Подписант")
    tourist_list = models.ManyToManyField(Tourist, related_name='tourist_list', verbose_name="Список туристов") 
    
    def __str__(self):
        return 'Договор №' + str(self.contract_num) + ' от ' + str(self.input_date) + ' - ' + str(self.client)

    