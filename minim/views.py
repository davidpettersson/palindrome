from rest_framework import viewsets

from minim.models import Message
from minim.palindrome import is_strict_palindrome, is_relaxed_palindrome
from minim.serializer import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-created')
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(
            is_strict_palindrome=is_strict_palindrome(serializer.validated_data['message']),
            is_relaxed_palindrome=is_relaxed_palindrome(serializer.validated_data['message'])
        )

    def perform_update(self, serializer):
        serializer.save(
            is_strict_palindrome=is_strict_palindrome(serializer.validated_data['message']),
            is_relaxed_palindrome=is_relaxed_palindrome(serializer.validated_data['message'])
        )
