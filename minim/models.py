from django.db import models


class Message(models.Model):
    MAXIMUM_MESSAGE_LENGTH = 256

    message = models.CharField(
        max_length=MAXIMUM_MESSAGE_LENGTH,
        help_text='Enter any message of maximum %d characters length.' % MAXIMUM_MESSAGE_LENGTH
    )
    is_strict_palindrome = models.BooleanField(
        editable=False,
        help_text='True if message is a strict palindrome, else false. Considers all characters, not only letters.'
    )
    is_relaxed_palindrome = models.BooleanField(
        editable=False,
        help_text='True if message is a relaxed palindrome, else false. Considers only alphanumerical characters, '
                  'disregards punctuation, spaces and other special characters.'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text='When the message was created.'
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        editable=False,
        help_text='When the message was last modified.'
    )
