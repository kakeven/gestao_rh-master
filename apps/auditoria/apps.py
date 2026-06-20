from django.apps import AppConfig


class AuditoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.auditoria'

#Apenas para carrega os signals ao iniciar
    def ready(self):
        import apps.auditoria.signals 