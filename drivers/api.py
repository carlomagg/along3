from rest_framework import viewsets, permissions
from drivers.models import Drivers
from .serializers import DriversSerializer

# Bookrides Viewset
class DriversViewSet(viewsets.ModelViewSet):
    queryset = Drivers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DriversSerializer