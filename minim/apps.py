from django.apps import AppConfig


class MinimConfig(AppConfig):
    name = 'minim'
    verbose_name = 'Minim Application'

    def ready(self):
        print('READY')
