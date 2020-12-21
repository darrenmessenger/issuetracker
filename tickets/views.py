# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketsForm

def get_tickets(request):
    """
    Create a view that will return a list of tickets that were published and 
    render them to 'issuetrackertickets.html' template
    """
    tickets = Ticket.objects.filter(published_date__lte=timezone.now
    ())
    return render(request, "issuetrackertickets.html", {'tickets':tickets})

def ticket_detail(request,pk):
    """
    Create a view that will return a single ticket object based on the ticket id 
    and render it to the 'ticketdetail.html' template
    """
    print("ticket detail")
    ticket = get_object_or_404(Ticket,pk=pk) 
    ticket.views +=1
    ticket.save()
    return render(request, "ticketdetail.html", {'ticket':ticket})

@login_required
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
            ticket.author = request.user.username
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketsForm(instance=ticket)
    return render(request, "issuetrackerticketform.html", {'form':form})
    
def ticket_vote(request,pk):
    """
    Create a view that will increase the upvotes for the current ticket
    and render it to the 'ticketdetail.html' template
    """
    ticket = get_object_or_404(Ticket,pk=pk) 
    ticket.upvotes +=1
    ticket.save()
    return render(request, "ticketdetail.html", {'ticket':ticket})
    
def ticket_vote_list(request,pk):
    """
    Create a view that will increase the upvotes for the current ticket in the list
    and render it to the 'ticketdetail.html' template
    """
    ticket = get_object_or_404(Ticket,pk=pk) 
    ticket.upvotes +=1
    ticket.save()
    tickets = Ticket.objects.filter(published_date__lte=timezone.now
    ())
    return render(request, "issuetrackertickets.html", {'tickets':tickets})