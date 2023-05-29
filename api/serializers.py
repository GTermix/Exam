from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from api.models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ticket_num = validated_data.get('ticket_num', instance.ticket_num)
        instance.date_avail = validated_data.get('date_avail', instance.date_avail)
        instance.date_flight = validated_data.get('date_flight', instance.date_flight)
        instance.date_depart = validated_data.get('date_depart', instance.date_depart)
        instance.date_land = validated_data.get('date_land', instance.date_land)
        instance.destination = validated_data.get('destination', instance.destination)
        # instance.save(user=self.context['request'].user)
        return instance


class ReadOnlyReservationSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    ticket = TicketSerializer()
    admin = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ('id',)

    def get_admin(self, obj):
        user = obj.admin
        admin_data = {
            'id': user.id,
            'name': user.username,
            'email': user.email
        }
        return admin_data

    # def create(self, validated_data):
    #     return Reservation.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.customer = validated_data.get('customer', instance.customer)
    #     instance.admin = validated_data.get('admin', instance.admin)
    #     instance.ticket = validated_data.get('ticket', instance.ticket)
    #     instance.date_res = validated_data.get('date_res', instance.date_res)
    #     instance.date_acc = validated_data.get('date_acc', instance.date_acc)
    #     instance.save()
    #     return instance


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.admin = validated_data.get('admin', instance.admin)
        instance.ticket = validated_data.get('ticket', instance.ticket)
        instance.date_res = validated_data.get('date_res', instance.date_res)
        instance.date_acc = validated_data.get('date_acc', instance.date_acc)
        instance.save()
        return instance

# class PostModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#
#
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(min_length=1, max_length=100)
#     description = serializers.CharField(max_length=1024)
#
#
# def encode():
#     model = PostModel(title="Nothing", description="desc")
#     model_sr = PostSerializer(model)
#     json = JSONRenderer().render(model_sr.data)
#     return json
#
#
# def decode():
#     response = io.BytesIO(b'{"title":"nthnh", "description":"desc"}')
#     data = JSONParser().parse(response)
#     serializer = PostSerializer(data=data)
#     serializer.is_valid()
#
#
# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     slug = serializers.SlugField()
#
#     def save(self):
#         title = self.validated_data.get('title')
#         slug = self.validated_data.get('slug')
#         instance = Category.objects.create(title=title, slug=slug)
#         return instance
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.save()
#         return instance
