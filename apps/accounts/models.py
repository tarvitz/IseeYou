# -*- coding: utf-8 -*-
from django.db import models
# your models here

# signals
from apps.accounts.signals import setup_signals
setup_signals()
