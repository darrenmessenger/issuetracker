# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Ticket, TicketComment

admin.site.register(Ticket)
admin.site.register(TicketComment)
