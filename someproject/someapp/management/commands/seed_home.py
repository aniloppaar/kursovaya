from django.core.management.base import BaseCommand
from someapp.models import Destination, Advantage, SiteSettings

class Command(BaseCommand):
    help = 'Заполняет базу данными для главной страницы'

    def handle(self, *args, **kwargs):
        if not SiteSettings.objects.exists():
            SiteSettings.objects.create()

        Destination.objects.all().delete()
        destinations = [
            {'title': 'Европа', 'tour_count': '24 тура', 'image': 'https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600', 'order': 1},
            {'title': 'Азия', 'tour_count': '18 туров', 'image': 'https://images.unsplash.com/photo-1528181304800-259b08848526?w=600', 'order': 2},
            {'title': 'Ближний Восток', 'tour_count': '12 туров', 'image': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=600', 'order': 3},
        ]
        for d in destinations:
            Destination.objects.create(**d)
        
        Advantage.objects.all().delete()
        advantages = [
            {'number': '01', 'title': 'Индивидуальный подход', 'description': 'Мы не верим в шаблоны. Каждый маршрут разрабатывается под ваши желания и бюджет.', 'order': 1},
            {'number': '02', 'title': 'Только проверенные места', 'description': 'Наши эксперты лично посещают отели и рестораны, прежде чем добавить их в программу.', 'order': 2},
            {'number': '03', 'title': 'Полное сопровождение', 'description': 'От покупки билетов до возвращения домой — ваш менеджер всегда на связи.', 'order': 3},
        ]
        for a in advantages:
            Advantage.objects.create(**a)

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены!'))