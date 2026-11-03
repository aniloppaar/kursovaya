from django.db import models

class Tour(models.Model):
    CATEGORY_CHOICES = [
        ('beach', 'Пляжный'),
        ('excursion', 'Экскурсионный'),
        ('city', 'Городской'),
        ('adventure', 'Приключенческий'),
    ]

    title = models.CharField('Название', max_length=200)
    country = models.CharField('Страна', max_length=100)
    city = models.CharField('Город', max_length=100)
    price = models.IntegerField('Цена (₽)')
    duration = models.IntegerField('Длительность (дней)')
    rating = models.FloatField('Рейтинг', default=5.0)
    image = models.ImageField('Фотография', upload_to='tours/', blank=True, null=True)
    description = models.TextField('Описание')
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='beach')
    included = models.TextField('Что включено в стоимость', blank=True, help_text="Каждую услугу пишите с новой строки")
    not_included = models.TextField('Не включено в стоимость', blank=True, help_text="Каждую услугу пишите с новой строки")
    itinerary = models.TextField('Программа по дням', blank=True, help_text="Например: День 1 - Прилет, заселение...")
    hotel_info = models.TextField('Информация об отелях', blank=True, help_text="Например: 5★ Rixos Premium...")
    important_info = models.TextField('Важная информация', blank=True, help_text="Например: Виза, страховка...")

    def __str__(self):
        return self.title

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer_name = models.CharField('ФИО', max_length=200)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    travelers_count = models.IntegerField('Туристов', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    booking_number = models.CharField('Номер брони', max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            import random
            self.booking_number = f"TD-{random.randint(10000000, 99999999)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Бронь {self.customer_name}"

class Destination(models.Model):
    title = models.CharField('Название', max_length=100)
    tour_count = models.CharField('Количество туров', max_length=50)
    image = models.ImageField('Фотография', upload_to='destinations/', blank=True, null=True)
    order = models.IntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Advantage(models.Model):
    number = models.CharField('Номер', max_length=10)
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание')
    order = models.IntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class SiteSettings(models.Model):
    hero_label = models.CharField('Надпись над заголовком', max_length=100, default='Новый взгляд на путешествия')
    hero_title = models.CharField('Главный заголовок', max_length=200, default='Искусство путешествовать')
    hero_subtitle = models.TextField('Подзаголовок', default='Продуманные маршруты, скрытые жемчужины и премиальный отдых.')
    phone = models.CharField('Телефон', max_length=50, default='+7 (999) 123-45-67')
    email = models.EmailField('Email', default='info@traveldream.ru')

    def __str__(self):
        return "Настройки сайта"