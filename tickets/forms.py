from django import forms
from tickets.models import Ticket

class TicketsForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'ticket_type', 'image', 'published_date']