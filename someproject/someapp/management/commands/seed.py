from django.core.management.base import BaseCommand
from someapp.models import Tour

class Command(BaseCommand):
    help = 'Заполняет базу тестовыми турами'

    def handle(self, *args, **options):
        Tour.objects.all().delete()
        
        tours_data = [
            {'title': 'Турция — Всё включено', 'country': 'Турция', 'city': 'Анталия', 'price': 65000, 'duration': 7, 'rating': 4.8, 'image': 'https://images.pexels.com/photos/3408744/pexels-photo-3408744.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Роскошный отдых на Средиземном море.', 'category': 'beach'},
            {'title': 'Египет — Пирамиды', 'country': 'Египет', 'city': 'Хургада', 'price': 55000, 'duration': 8, 'rating': 4.6, 'image': 'https://images.pexels.com/photos/364980/pexels-photo-364980.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Отдых на Красном море с экскурсией к пирамидам.', 'category': 'beach'},
            {'title': 'Италия — Рим и Венеция', 'country': 'Италия', 'city': 'Рим', 'price': 120000, 'duration': 10, 'rating': 4.9, 'image': 'https://images.pexels.com/photos/2064827/pexels-photo-2064827.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Путешествие по историческим городам.', 'category': 'excursion'},
            {'title': 'Тайланд — Экзотика', 'country': 'Тайланд', 'city': 'Пхукет', 'price': 85000, 'duration': 12, 'rating': 4.7, 'image': 'https://images.pexels.com/photos/1268855/pexels-photo-1268855.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Тропический рай.', 'category': 'beach'},
            {'title': 'Франция — Париж', 'country': 'Франция', 'city': 'Париж', 'price': 110000, 'duration': 6, 'rating': 4.9, 'image': 'https://images.pexels.com/photos/2082103/pexels-photo-2082103.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Романтическое путешествие.', 'category': 'excursion'},
            {'title': 'ОАЭ — Дубай', 'country': 'ОАЭ', 'city': 'Дубай', 'price': 95000, 'duration': 7, 'rating': 4.8, 'image': 'https://images.pexels.com/photos/1470502/pexels-photo-1470502.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Роскошь и небоскрёбы.', 'category': 'city'},
            {'title': 'Испания — Барселона', 'country': 'Испания', 'city': 'Барселона', 'price': 105000, 'duration': 9, 'rating': 4.7, 'image': 'https://images.pexels.com/photos/1388030/pexels-photo-1388030.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Гауди и пляжи.', 'category': 'city'},
            {'title': 'Мальдивы — Райский отдых', 'country': 'Мальдивы', 'city': 'Мале', 'price': 250000, 'duration': 10, 'rating': 5.0, 'image': 'https://images.pexels.com/photos/1287460/pexels-photo-1287460.jpeg?auto=compress&cs=tinysrgb&w=800', 'description': 'Бунгало над водой.', 'category': 'beach'},
        ]

        for data in tours_data:
            Tour.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Успешно создано туров: {len(tours_data)}!'))