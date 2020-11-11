# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketsForm

def get_tickets(request):
    """
    Create a view that will return a list of tickets that were published and 
    render them to 'tickets.html' template
    """
    tickets = Ticket.objects.filter(published_date__lte=timezone.now
    ())
    return render(request, "issuetrackertickets.html", {'tickets':tickets})

def ticket_detail(request,pk):
    """
    Create a view that will return a single ticket object based on the ticket id 
    and render it to the 'show_tickets.html' template
    """
    ticket = get_object_or_404(Ticket,pk=pk) 
    ticket.views +=1
    ticket.save()
    return render(request, "ticketdetail.html", {'ticket':ticket})

def create_or_edit_ticket(request, pk=None):
    """
    Create a view that allows us to create or edit a ticket depending if 
    the tickets id is null or not. 
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketsForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketsForm(instance=ticket)
    return render(request, "issuetrackerticketform.html", {'form':form})