# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    """
    Add a ticket
    """
    TYPE_CHOICES = (
        ('BUG', 'Bug'),
        ('NEW FEATURE', 'New feature')
    )
    STATUS_CHOICES = (
        ('TO_DO', 'To do'),
        ('UNDER_REVIEW', 'Under Review'),
        ('DECLINED', 'Declined'),
        ('PLANNED', 'Planned'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    )
    title = models.CharField(max_length=225,blank=False)
    author = models.CharField(max_length=150, default='')
    content = models.TextField()
    ticket_type = models.CharField(choices=TYPE_CHOICES, default='BUG', max_length=11)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='TO_DO', max_length=12)

    def __unicode__(self):
        return self.title
    
class TicketComment(models.Model):
    """Model that can create comments"""
    author = models.CharField(max_length=150, default='')
    comment = models.TextField(blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)    
        
    def __str__(self):
        return self.author