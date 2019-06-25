from rest_framework import serializers

from minim.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'id', 'message', 'is_strict_palindrome', 'is_relaxed_palindrome', 'created', 'last_modified')
