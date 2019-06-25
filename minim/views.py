from rest_framework import viewsets

from minim.models import Message
from minim.serializer import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-created')
    serializer_class = MessageSerializer
