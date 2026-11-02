from django.contrib import admin
from .models import Tour, Booking, Destination, Advantage, SiteSettings

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city', 'price', 'rating', 'category')
    search_fields = ('title', 'country', 'city')
    list_filter = ('category', 'country')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'tour', 'email', 'phone', 'created_at')
    search_fields = ('customer_name', 'email', 'phone')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'tour_count', 'order')
    list_editable = ('order',)

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')
    list_editable = ('order',)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()