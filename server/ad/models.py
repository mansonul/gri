#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import smart_unicode
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from datetime import timedelta
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default='')

    def __unicode__(self):
        return smart_unicode(self.title)

class Ad(models.Model):
    user = models.ForeignKey(User)

    ### User defined fields
    title = models.CharField(max_length=40, null=False, blank=False, default='')
    slug = AutoSlugField(populate_from='title', unique=True)

    description = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?\d{9,15}$',
                                 message="Numărul de telefon trebuie să fie în formatul: '+999999999'. Se acceptă doar cifre.")
    phone = models.CharField(max_length=15, validators=[phone_regex, ], null=True, blank=True)
    website = models.URLField(max_length=40, null=True, blank=True)
    facebook = models.URLField(max_length=60, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=150, blank=True, default='')
    category = models.ForeignKey(Category, blank=True, null=True, related_name='category')


    ### Time management
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    aprooved = models.DateTimeField(null=True, blank=True)
    duration = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')



    def __unicode__(self):
        return smart_unicode(self.title)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    # def clean(self):
    #     if self.status == 'd' and self.aprooved == None:
    #         self.duration = None
    #     elif self.status == 'p' and self.aprooved != None:
    #         self.duration = self.aprooved + timedelta(days=14)
    #     elif self.status == 'd' and self.aprooved != None:
    #         self.duration
    #
    #     if self.updated != self.timestamp and self.status == 'p':
    #         self.status = 'd'