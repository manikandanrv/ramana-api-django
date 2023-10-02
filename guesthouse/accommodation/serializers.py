
from rest_framework import serializers
from accommodation.models import Devotee,Room, Request, Checkin
from django.contrib.auth.models import User



##Auth Section - User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']

##Master data serializers -  Devotee, Rooms, etc.
class DevoteeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Devotee
        fields = ['id', 'first_name', 'last_name', 'email', 'mobile', 'aadhar_no','passport_no'
        , 'address_building', 'address_doorno', 'address_line1', 'address_line2', 'address_city'
        ,'address_state', 'address_country', 'nationality', 'owner']

class RoomSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Room
        fields = ['id', 'room_number','guesthouse_name','room_type','max_guest_in_room',
                'is_room_booked','is_room_dirty','created']

##Transactional Serializers - Requests, Checkins, Checkouts etc
class RequestSerializer(serializers.ModelSerializer):
    #devotee = serializers.ReadOnlyField(source='devotee.email')
    approver = serializers.ReadOnlyField(source='approver.username')

    class Meta:
        model = Request
        fields = ['id', 'devotee','likely_arrival','likely_departure','no_of_guests','purpose',
        'is_request_approved','approver','created']

class CheckinSerializer(serializers.ModelSerializer):
    #devotee = serializers.ReadOnlyField(source='devotee')
    checkin_by = serializers.ReadOnlyField(source='checkin_by.username')

    class Meta:
        model = Checkin
        fields = ['id', 'devotee','checkin_date','likely_checkout_date','is_checkout_completed','actual_checkout_date','no_of_guests','rooms','guests',
        'is_foreign_devotee','checkin_by','created']

    def update(self, instance, validated_data):
        instance_meta = instance.meta.copy()
        instance_meta.update(validated_data.get("meta", {}))
        validated_data["meta"] = instance_meta
        return super().update(instance, validated_data)


# class AllotmentSerializer(serializers.ModelSerializer):
#     #devotee = serializers.ReadOnlyField(source='devotee.email')
#     approver = serializers.ReadOnlyField(source='approver.username')

#     class Meta:
#         model = Allotment
#         fields = ['id', 'devotee','likely_arrival','likely_departure','no_of_guests','purpose',
#         'is_request_approved','approver','created']
