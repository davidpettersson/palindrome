from django.apps import AppConfig



class MinimConfig(AppConfig):
    name = 'minim'
    verbose_name = 'Minim Application'

    def ready(self):
        # Added here to ensure that the signals module is loaded and the
        # dependency not removed by the IDE when performing import optimization.
        from minim.signals import palindrome_checker
        _ = palindrome_checker
