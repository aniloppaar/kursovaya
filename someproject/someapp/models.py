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
    image = models.URLField('Ссылка на фото')
    description = models.TextField('Описание')
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='beach')

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