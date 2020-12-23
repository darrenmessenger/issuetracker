from django import forms
from tickets.models import Ticket, TicketComment

class TicketsForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'ticket_type', 'image', 'published_date']
        
class TicketCommentForm(forms.ModelForm):
    """Form for creating comments"""
    class Meta:
        model = TicketComment
        fields = ('comment', )