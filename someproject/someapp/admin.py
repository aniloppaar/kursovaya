from django.contrib import admin
from .models import Tour, Booking, Destination, Advantage, SiteSettings, TourDetail, TourProgram

class TourDetailInline(admin.StackedInline):
    model = TourDetail
    can_delete = False
    verbose_name = 'Детали тура'
    verbose_name_plural = 'Детали тура'

class TourProgramInline(admin.TabularInline):
    model = TourProgram
    extra = 1
    verbose_name = 'День программы'
    verbose_name_plural = 'Программа по дням'

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city', 'price', 'rating', 'category')
    search_fields = ('title', 'country', 'city')
    list_filter = ('category', 'country')
    inlines = [TourDetailInline, TourProgramInline]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'tour', 'email', 'phone', 'created_at')
    search_fields = ('customer_name', 'email', 'phone')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'tour_count', 'order')

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()