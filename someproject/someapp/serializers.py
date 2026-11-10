from rest_framework import serializers
from .models import Tour, Booking, Destination, Advantage, SiteSettings, TourDetail, TourProgram

class TourDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDetail
        fields = '__all__'

class TourProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourProgram
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    details = TourDetailSerializer(read_only=True)
    program = TourProgramSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if instance.image and request:
            representation['image'] = request.build_absolute_uri(instance.image.url)
        return representation

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if instance.image and request:
            representation['image'] = request.build_absolute_uri(instance.image.url)
        return representation

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'