import json
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.generics import GenericAPIView


class CustomerDetailCreateView(GenericAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def post(self, req):
        serializer = self.get_serializer_class()(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req):
        serializer = self.get_serializer_class()(Customer.objects.all(), many=True)
        return Response(data=serializer.data)


class CustomerDeleteEditView(GenericAPIView):
    lookup_field = 'pk'
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, req, pk):
        cat = get_object_or_404(Customer, pk=pk)
        serializer = self.get_serializer_class()(cat)
        return Response(data=serializer.data)

    def patch(self, req, pk):
        cat = get_object_or_404(Customer, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, req, pk):
        cat = get_object_or_404(Customer, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        cat = get_object_or_404(Customer, pk=pk)
        cat.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class ReservationDetailCreateView(GenericAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def post(self, req):
        serializer = self.get_serializer_class()(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req):
        serializer = ReadOnlyReservationSerializer(Reservation.objects.all(), many=True)
        return Response(data=serializer.data)


class ReservationDeleteEditView(GenericAPIView):
    lookup_field = 'pk'
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def get(self, req, pk):
        cat = get_object_or_404(Reservation, pk=pk)
        serializer = ReadOnlyReservationSerializer(cat)
        return Response(data=serializer.data)

    def patch(self, req, pk):
        cat = get_object_or_404(Reservation, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, req, pk):
        cat = get_object_or_404(Reservation, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        cat = get_object_or_404(Reservation, pk=pk)
        cat.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class TicketDetailCreateView(GenericAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def post(self, req):
        serializer = self.get_serializer_class()(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req):
        serializer = self.get_serializer_class()(Ticket.objects.all(), many=True)
        return Response(data=serializer.data)


class TicketDeleteEditView(GenericAPIView):
    lookup_field = 'pk'
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get(self, req, pk):
        cat = get_object_or_404(Ticket, pk=pk)
        serializer = self.get_serializer_class()(cat)
        return Response(data=serializer.data)

    def patch(self, req, pk):
        cat = get_object_or_404(Ticket, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, req, pk):
        cat = get_object_or_404(Ticket, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        cat = get_object_or_404(Ticket, pk=pk)
        cat.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)
