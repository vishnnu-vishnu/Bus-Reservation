
from rest_framework import serializers
from Manager.models import Busoperator,Category,Buses,Offer,Review,Reservation,Payment

class OperatorSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Busoperator
        fields=["id","username","email","password","phone","name","description","address","website","logo"]

    def create(self, validated_data):
        return Busoperator.objects.create_user(**validated_data)
    
class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    is_active=serializers.BooleanField(read_only=True)
    class Meta:
        model = Category
        fields =["id","name","is_active"]

class BusSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    is_active=serializers.BooleanField(read_only=True)
    class Meta:
        model = Buses
        fields = ["id","name","description","price","image","is_active","category","boarding_point","boarding_time","dropping_point","dropping_time","duration","capacity"]
    

class OfferSerializer(serializers.ModelSerializer):
    bus=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    busoperators=serializers.CharField(read_only=True)
    class Meta:
        model = Offer
        fields="__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields="__all__"


