from django.apps import AppConfig


class CongressConfig(AppConfig):
    name = 'congress'

    def ready(self):
        import congress.signals
