from django import forms
from tickets.models import add_tickets

class ticketsForm(forms.ModelForm):
    class Meta:
        model = add_tickets
        fields = ['title','content','published_date','views']