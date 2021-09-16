import logging
from django.urls import path
from .views import new_view


log = logging.getLogger(__name__)

urlpatterns = [
    path('', new_view, name='new-view')
]

log.info('Calling URL')
