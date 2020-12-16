from django import forms

class MakePaymentForm(forms.Form):
    print("MakePaymentForm...")
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2040)]
    
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label ='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month",choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='year',choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput,  required=False)
    print("End of MakePaymentForm...")
