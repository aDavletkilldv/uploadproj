import logging
from django.apps import AppConfig


log = logging.getLogger(__name__)


class NewappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newapp'


log.info('Calling a class NewappConfig')
