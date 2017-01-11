# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Coffee(models.Model):

    # Attributes
    title = models.CharField(
        _('title'),
        max_length=200,
        unique=True,
    )
    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=20
    )

    # Metadata
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Functions
    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return u"%s" % (self.title)


class Color(models.Model):

    # Attributes
    name = models.CharField(
        _('name'),
        max_length=200,
        unique=True,
    )
    image = models.ImageField(
        _('image'),
        blank=False,
        null=False,
        upload_to='colors/%Y/%m/%d'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=20
    )

    # Metadata
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Functions
    def __unicode__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % (self.name)


class Package(models.Model):

    # Choices
    # POSITION_CHOICES = (
    #     ('t', _('Top')),
    #     ('b', _('Bottom')),
    #     ('l', _('Left')),
    #     ('r', _('Right')),
    #     ('c', _('Center')),
    #     )

    # Relations
    coffee = models.ForeignKey(
        Coffee,
        verbose_name=_('coffee'),
        related_name='packagebycoffee',
    )
    color = models.OneToOneField(
        Color,
        verbose_name=_('color'),
        related_name='packagebycolor',
    )
    # product = models.ForeignKey(
    #     Product,
    #     verbose_name=_('product'),
    #     related_name='packagebyproduct',
    # )
    # order = models.ForeignKey(
    #     Order,
    #     verbose_name=_('order'),
    #     related_name='packagebyorder',
    # )

    # Attributes
    # title = models.CharField(
    #     _('title'),
    #     max_length=200,
    #     unique=True,
    #     blank=True,
    #     null=True,
    # )
    slug = models.SlugField(
        _('slug'),
        editable=False,
        unique=True
    )
    image = models.ImageField(
        _('image'),
        blank=False,
        null=False,
        upload_to='images/%Y/%m/%d'
    )
    # position = models.CharField(
    #     _('position'),
    #     choices=POSITION_CHOICES,
    #     max_length=1,
    #     blank=True,
    # )
    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        _('active'),
        default=True,
    )

    # Metadata
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Functions
    def __unicode__(self):
        return self.id

    def __unicode__(self):
        return u"%s" % (self.id)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super(Package, self).save(*args, **kwargs)

    # Meta
    class Meta:
        ordering = ['id']
        verbose_name = _('package')
        verbose_name_plural = _('packages')
