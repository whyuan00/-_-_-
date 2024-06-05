from django.apps import AppConfig
from django.core.signals import request_started
# from .views import update_exchange_rate_json

class ExchangeRateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exchange_rate'

    # def ready(self):
    #     request_started.connect(update_exchange_rate_json)
