from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated & IsAdminOrReadOnly]
