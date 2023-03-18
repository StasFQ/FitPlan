from django import forms


class ContactUs(forms.Form):
    subject = forms.CharField(max_length=230)
    text = forms.CharField(widget=forms.Textarea)
