from django.db import models
import datetime


# Create your models here.
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


class TourOperator(models.Model):
    class Meta:
        verbose_name = "Туроператор"
        verbose_name_plural = "Туроператоры"
        
    operator_name = models.CharField(max_length=200, verbose_name="Название")
    registry_num = models.CharField(max_length=50, verbose_name="Реестровый номер")
    full_name = models.CharField(max_length=200, verbose_name="Полное наименование")
    short_name = models.CharField(max_length=50, verbose_name="Сокращеннное наименование")
    fact_address = models.CharField(max_length=200, verbose_name="Место нахождения")
    post_address = models.CharField(max_length=200, verbose_name="Почтовый адрес")
    www_address = models.CharField(max_length=50, verbose_name='Адрес сайта в сети "Интернет"')
    tourpom_member = models.BooleanField(verbose_name='Является членом ассоциации  "ТУРПОМОЩЬ"')
    inn = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="ИНН")
    ogrn = models.DecimalField(max_digits=13, decimal_places=0, verbose_name="ОГРН") 
    #assurer
    
    def __str__(self):
        return self.operator_name


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
        
    office_name = models.CharField(max_length=200, verbose_name="Наименование")
    office_adddress = models.CharField(max_length=200, verbose_name="Адрес")
    office_city = models.CharField(max_length=50, verbose_name="Город")

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
        
    contract_num = models.IntegerField(unique_for_month = "contract_date", verbose_name="Номер договора")
    contract_date = models.DateField(blank=True, null=True, verbose_name="Дата договора")
    #contract_num = models.IntegerField(unique_for_year = "input_date", True, verbose_name="Номер договора")
    #input_date = models.DateField(blank=True, null=True, auto_now_add=True, verbose_name="Дата ввода")
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
    contract_sum = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True, verbose_name="Сумма контракта")
    prepayment_sum = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True, verbose_name="Сумма предоплаты")
    signatory = models.ForeignKey(Manager, models.PROTECT, related_name='contract_signatory', blank=True, null=True, verbose_name="Подписант")
    tourist_list = models.ManyToManyField(Tourist, related_name='tourist_list', verbose_name="Список туристов") 
    
    tour_orepator = models.ForeignKey(TourOperator, models.PROTECT, blank=True, null=True, verbose_name="Туроператор")
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

    
    
    
    
    
    

#class City(models.Model):
#    class Meta:
#        verbose_name = "Город"
#        verbose_name_plural = "Города"
#        
#    city_name = models.CharField(max_length=200, verbose_name="Название")
#    
#    def __str__(self):
#        return self.city_name