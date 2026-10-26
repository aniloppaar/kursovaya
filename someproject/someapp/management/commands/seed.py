from django.core.management.base import BaseCommand
from someapp.models import Tour

class Command(BaseCommand):
    help = 'Заполняет базу тестовыми турами'

    def handle(self, *args, **options):
        # Очищаем старые данные
        Tour.objects.all().delete()
        
        tours_data = [
            {'title': 'Турция — Всё включено', 'country': 'Турция', 'city': 'Анталия', 'price': 65000, 'duration': 7, 'rating': 4.8, 'image': 'https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800', 'description': 'Роскошный отдых на Средиземном море.', 'category': 'beach'},
            {'title': 'Египет — Пирамиды', 'country': 'Египет', 'city': 'Хургада', 'price': 55000, 'duration': 8, 'rating': 4.6, 'image': 'https://images.unsplash.com/photo-1539768942893-daf53e448371?w=800', 'description': 'Отдых на Красном море с экскурсией.', 'category': 'beach'},
            {'title': 'Италия — Рим и Венеция', 'country': 'Италия', 'city': 'Рим', 'price': 120000, 'duration': 10, 'rating': 4.9, 'image': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800', 'description': 'Путешествие по историческим городам.', 'category': 'excursion'},
            {'title': 'Тайланд — Экзотика', 'country': 'Тайланд', 'city': 'Пхукет', 'price': 85000, 'duration': 12, 'rating': 4.7, 'image': 'https://images.unsplash.com/photo-1528181304800-259b08848526?w=800', 'description': 'Тропический рай.', 'category': 'beach'},
            {'title': 'Франция — Париж', 'country': 'Франция', 'city': 'Париж', 'price': 110000, 'duration': 6, 'rating': 4.9, 'image': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800', 'description': 'Романтическое путешествие.', 'category': 'excursion'},
            {'title': 'ОАЭ — Дубай', 'country': 'ОАЭ', 'city': 'Дубай', 'price': 95000, 'duration': 7, 'rating': 4.8, 'image': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800', 'description': 'Роскошь и небоскрёбы.', 'category': 'city'},
            {'title': 'Мальдивы — Рай', 'country': 'Мальдивы', 'city': 'Мале', 'price': 250000, 'duration': 10, 'rating': 5.0, 'image': 'https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=800', 'description': 'Бунгало над водой.', 'category': 'beach'},
        ]

        for data in tours_data:
            Tour.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Успешно создано {len(tours_data)} туров!'))