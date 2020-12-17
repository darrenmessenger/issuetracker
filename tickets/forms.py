from django import forms
from tickets.models import Ticket

class TicketsForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'image', 'published_date']