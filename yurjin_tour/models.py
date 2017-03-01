from django.db import models
from django.contrib.auth.models import User

import datetime
from number_to_text import num2text
from math import modf


from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Entity(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=200, verbose_name="Название")
    full_name = models.CharField(blank=True, max_length=200, verbose_name="Полное наименование")
    short_name = models.CharField(blank=True, max_length=200, verbose_name="Краткое наименование")
    fact_address = models.CharField(blank=True, max_length=200, verbose_name="Место нахождения")
    post_address = models.CharField(blank=True, max_length=200, verbose_name="Почтовый адрес")    
    inn = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=0, verbose_name="ИНН")
    kpp = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=0, verbose_name="КПП")
    ogrn = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=0, verbose_name="ОГРН")
    account = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=0, verbose_name="Расчетный счет")
    corr_account = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=0, verbose_name="Корр. счет")
    phone =  models.CharField(blank=True, max_length=200, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="e-mail")
    
    
    def __str__(self):
        return self.name
   
   
class Person(models.Model):
    class Meta:
        abstract = True
        
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    mid_name = models.CharField(max_length=200, verbose_name="Отчество")
    full_name_r = models.CharField(blank=True, max_length=200, verbose_name="ФИО в родительном падеже")

    def get_fio(self):
        if ((self.last_name + self.first_name + self.mid_name).strip() == ''):
            fio = self.user.username
        else:
            fio = self.last_name + ' ' + self.first_name[0] + '.' + self.mid_name[0]+'.'
        
        return fio 
    
    def get_full_name(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.mid_name
    
    def __str__(self):
        return self.get_fio()
 

class TourOperator(Entity):
    class Meta:
        verbose_name = "Туроператор"
        verbose_name_plural = "Туроператоры"
        
    registry_num = models.CharField(max_length=50, verbose_name="Реестровый номер")
    www_address = models.CharField(max_length=50, verbose_name='Адрес сайта в сети "Интернет"')
    tourpom_member = models.BooleanField(verbose_name='Является членом ассоциации  "ТУРПОМОЩЬ"') 
    #assurer_name

    
class TourAgency(Entity):
    class Meta:
        verbose_name = "Турагентство"
        verbose_name_plural = "Турагентства"
    
    director = models.ForeignKey("Manager", null=True, verbose_name='Директор')


class Country(models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        
    country_name = models.CharField(max_length=200, verbose_name="Название")
    
    def __str__(self):
        return self.country_name


class Resort(models.Model):
    class Meta:
        verbose_name = "Курорт"
        verbose_name_plural = "Курорты"
        
    resort_name = models.CharField(max_length=200, verbose_name="Название")
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Страна")

    def __str__(self):
        return self.resort_name
    

class RoomType(models.Model):
    class Meta:
        verbose_name = "Тип номера"
        verbose_name_plural = "Типы номеров"
    
    room_type_name = models.CharField(max_length=50, verbose_name='Название')
    room_type_description = models.CharField(blank=True,max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.room_type_name

    
class Board(models.Model):
    class Meta:
        verbose_name = "Тип питания"
        verbose_name_plural = "Типы питания"
    
    board_code = models.CharField(max_length=3, verbose_name='Код')
    board_name = models.CharField(max_length=25, verbose_name='Название')
    board_description = models.CharField(blank=True,max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.board_code


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
        
    tour_agency = models.ForeignKey(TourAgency, null=True,blank=True)
    office_name = models.CharField(max_length=200, verbose_name="Наименование")
    office_adddress = models.CharField(max_length=200, verbose_name="Адрес")
    office_city = models.CharField(max_length=50, verbose_name="Город")
    
    #signatory = models.ForeignKey(Manager, models.PROTECT, related_name='contract_signatory', blank=True, null=True, verbose_name="Подписант")
    #office_chief_r = models.CharField(max_length=200, verbose_name="В лице кого")

    def __str__(self):
        return self.office_name
    
    
class Status(models.Model):
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        
    status_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.status_name


class Manager(Person):
    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"
        
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    manager_office = models.ForeignKey(Office, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Офис")
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Manager.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.manager.save()


class Tourist(Person):
    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристы"

    birthdate = models.DateField(verbose_name="Дата рождения")
    passport_num = models.CharField(max_length=200, verbose_name="Номер паспорта РФ")
    passport_date = models.DateField(verbose_name="Дата выдачи паспорта РФ")
    passport_issued_by = models.CharField(max_length=50, verbose_name="Кем выдан паспорт РФ")
    international_passport = models.CharField(max_length=200, verbose_name="Загранпаспорт")
    international_name = models.CharField(max_length=200, verbose_name="Имя как в загранпаспорте")
    international_passport_date_of_expiry=models.DateField(verbose_name="Срок действия загранпаспорта")
    phone = models.CharField(blank=True, max_length=50, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="e-mail")
    address = models.CharField(blank=True, max_length=200, verbose_name="Адрес")
    



class Contract(models.Model):
    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"
        
    contract_num = models.IntegerField(unique_for_month = "contract_date", verbose_name="Номер договора")
    contract_date = models.DateField(blank=True, null=True, verbose_name="Дата договора")
    manager = models.ForeignKey(Manager, models.PROTECT, blank=True, null=True, verbose_name="Менеджер")
    office = models.ForeignKey(Office, models.PROTECT, blank=True, null=True, verbose_name="Офис")
    client = models.ForeignKey(Tourist, models.PROTECT, blank=True, null=True, verbose_name="Клиент")
    #airport_from1 = models.ForeignKey(Airport, models.PROTECT, related_name='airport_from1', blank=True, null=True, verbose_name="Аэропорт отправления туда")
    #airport_to1 = models.ForeignKey(Airport, models.PROTECT, related_name='airport_to1', blank=True, null=True, verbose_name="Аэропорт прибытия туда")
    #airport_from2 = models.ForeignKey(Airport, models.PROTECT, related_name='airport_from2', blank=True, null=True, verbose_name="Аэропорт отправления обратно")
    #airport_to2 = models.ForeignKey(Airport, models.PROTECT, related_name='airport_to2', blank=True, null=True, verbose_name="Аэропорт прибытия обратно")
    status = models.ForeignKey(Status, models.PROTECT, blank=True, null=True, verbose_name="Статус")
    
    tour_begin_date = models.DateField(blank=True, null=True, verbose_name="Дата начала тура")
    tour_finish_date = models.DateField(blank=True, null=True, verbose_name="Дата окончания тура")
    contract_sum = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, verbose_name="Сумма контракта")
    prepayment_sum = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, verbose_name="Сумма предоплаты")
    signatory = models.ForeignKey(Manager, models.PROTECT, related_name='contract_signatory', blank=True, null=True, verbose_name="Подписант")
    tourist_list = models.ManyToManyField(Tourist, related_name='tourist_list', verbose_name="Список туристов") 
    
    tour_operator = models.ForeignKey(TourOperator, models.PROTECT, blank=True, null=True, verbose_name="Туроператор")
    resort =  models.ForeignKey(Resort, models.PROTECT, blank=True, null=True, verbose_name="Курорт")
    
    hotel_name = models.CharField(blank=True, max_length=200, verbose_name="Название отеля")
    hotel_begin_date = models.DateField(blank=True, null=True, verbose_name="Дата въезда в отель")
    hotel_finish_date = models.DateField(blank=True, null=True, verbose_name="Дата выезда из отеля")
    room_type = models.ForeignKey(RoomType, models.PROTECT, blank=True, null=True, verbose_name="Тип номера")
    board = models.ForeignKey(Board, models.PROTECT, blank=True, null=True, verbose_name="Тип питания")
    
    transfer = models.BooleanField(blank=True, verbose_name="Включена перевозка наземным транспортом")
    excursion = models.BooleanField(blank=True, verbose_name="Включена экскурсионная программа")
    russian_guide = models.BooleanField(blank=True, verbose_name="Включена встреча и проводы с русскоговорящим гидом")
    visa_support = models.BooleanField(blank=True, verbose_name="Включена визовая поддержка")
    medical_insurance = models.BooleanField(blank=True, verbose_name="Включена медицинская страховка")
    non_departure_insurance = models.BooleanField(blank=True, verbose_name="Включена страховка от невыезда")
    
    
    doc_get_date = models.DateField(blank=True, null=True, verbose_name="Дата получения документов клиентом")
    
    def __str__(self):
        return 'Договор №' + self.contract_date.strftime('%m%y') + '-' + str(self.contract_num) + ' от ' + str(self.contract_date) + ' - ' + str(self.client)

    def get_hotel_nights(self):
        return (self.hotel_finish_date-self.hotel_begin_date).days
    
    def get_payment_sum(self):
        return self.contract_sum - self.prepayment_sum
    
    def get_contract_sum_string(self):
        rub = ((u'рубль', u'рубля', u'рублей'), 'm')
        kop = ((u'копейка', u'копейки', u'копеек'), 'f')
        #sum_str = num2text(self.contract_sum, rub)
        #sum_str = sum_str + ' ' + num2text((self.contract_sum - int(self.contract_sum))*100, kop)
        #sum_str = num2text((self.contract_sum - int(self.contract_sum))*100, female_units)
        #sum_str=self.contract_sum
        sum_arr = modf(self.contract_sum)
        sum_str = num2text(sum_arr[1],rub)+' '+num2text(sum_arr[0]*100,kop)
        return sum_str
    

    

#class City(models.Model):
#    class Meta:
#        verbose_name = "Город"
#        verbose_name_plural = "Города"
#        
#    city_name = models.CharField(max_length=200, verbose_name="Название")
#    
#    def __str__(self):
#        return self.city_name
