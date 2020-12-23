# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-23 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_ticket_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=150)),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.Ticket')),
            ],
        ),
    ]
