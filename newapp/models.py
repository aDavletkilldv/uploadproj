import logging
from django.db import models


log = logging.getLogger(__name__)


class Image(models.Model):
    log.info('Calling a model Image')
    imgfile = models.ImageField(upload_to='files')
