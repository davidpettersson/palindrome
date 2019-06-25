from django.db.models.signals import pre_save
from django.dispatch import receiver

from minim.models import Message
from minim.palindrome import is_strict_palindrome, is_relaxed_palindrome


@receiver(pre_save, sender=Message)
def palindrome_checker(sender, instance, **kwargs):
    print("SIGNAL!")
    instance.is_strict_palindrome = is_strict_palindrome(instance.message)
    instance.is_relaxed_palindrome = is_relaxed_palindrome(instance.message)
