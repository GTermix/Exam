from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', CustomerDetailCreateView.as_view(), name='cr_cat'),
    path('customer/<int:pk>/', CustomerDeleteEditView.as_view(), name='sdfsd'),
    path('tickets/', TicketDetailCreateView.as_view(), name='crt_cat'),
    path('ticket/<int:pk>/', TicketDeleteEditView.as_view(), name='tsdfsd'),
    path('reservations/', ReservationDetailCreateView.as_view(), name='crr_cat'),
    path('reservation/<int:pk>/', ReservationDeleteEditView.as_view(), name='rsdfsd'),
]
