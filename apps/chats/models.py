# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from model_utils.models import TimeStampedModel


class Chat(TimeStampedModel):
    from_addr = models.ForeignKey(get_user_model(), related_name='message_from', on_delete=models.DO_NOTHING)
    to_addr = models.ForeignKey(get_user_model(), related_name='message_to', on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('chat:list')


class Message(TimeStampedModel):
    body = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.body[:50] + '...'

    def get_absolute_url(self):
        return reverse('chat:list')
