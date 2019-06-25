from rest_framework import serializers

from minim.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'is_strict_palindrome', 'is_relaxed_palindrome')
