import os
from django.apps import AppConfig

default_app_config = 'app01.app01Config'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class app01Config(AppConfig):
    name = 'app01'
    verbose_name = "app01"