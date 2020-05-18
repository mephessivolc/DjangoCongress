from django.apps import AppConfig


class CongressConfig(AppConfig):
    name = 'congress'
    verbose_name = 'Evento'
    verbose_name_plural = 'Eventos'
    
    def ready(self):
        import congress.signals
