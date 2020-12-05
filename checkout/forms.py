from django import forms

class MakePaymentForm(forms.Form):
    month_choices = [(i,i) for i in range(1,13)]
    year_choices = [(i,i) for i in range(2018,2040)]
    
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label ='Security Code', required=False)
    expiry_month = forms.ChoiceField(label="Month",choices=month_choices, required=False)
    expiry_year = forms.ChoiceField(label='year',choices=year_choices, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)