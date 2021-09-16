import logging
from django.apps import apps
from django.contrib import admin


for model in apps.get_app_config('newapp').get_models():
    admin.site.register(model)
