import logging
from django import forms


log = logging.getLogger(__name__)


class ImageForm(forms.Form):
    log.info('Calling a form ImageForm')
    imgfile = forms.ImageField(label='Выберите изображение')
