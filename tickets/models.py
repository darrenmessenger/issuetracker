# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class add_tickets(models.Model):
    """
    Add tickets
    """
    title = models.CharField(max_length=225,blank=False)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title