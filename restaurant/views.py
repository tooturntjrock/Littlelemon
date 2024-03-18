from django.shortcuts import render
from .models import Booking, Menu
from rest_framework import generics, viewsets
from .serializers import menuSerializer, bookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    search_fields = ["category__title"]
    ordering_fields = ["price", "inventory"]

    

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
