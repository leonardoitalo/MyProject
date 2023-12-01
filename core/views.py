from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Cliente
from .serializars import ClienteSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ClienteSerializer