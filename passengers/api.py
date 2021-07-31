from rest_framework import viewsets, permissions
from passengers.models import Passengers
from .serializers import PassengersSerializer

# Bookrides Viewset
class PassengersViewSet(viewsets.ModelViewSet):
    queryset = Passengers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PassengersSerializer