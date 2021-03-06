# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory

from ..accounts.factories import UserFactory
from .models import Comment


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = factory.Faker('text')
