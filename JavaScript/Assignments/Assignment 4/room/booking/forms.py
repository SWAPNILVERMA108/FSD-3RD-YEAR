from datetime import date

from django import forms


class SearchForm(forms.Form):
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    guests = forms.IntegerField(label='Attendees', min_value=1, max_value=200, initial=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned = super().clean()
        check_in, check_out = cleaned.get('check_in'), cleaned.get('check_out')
        if check_in and check_in < date.today():
            self.add_error('check_in', 'Choose today or a future date.')
        if check_in and check_out and check_out <= check_in:
            self.add_error('check_out', 'Check-out must be after check-in.')
        return cleaned


class BookingForm(forms.Form):
    guest_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'name', 'class': 'form-control'}))
    guest_email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))
    guests = forms.IntegerField(label='Attendees', min_value=1, max_value=200, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    def clean(self):
        cleaned = super().clean()
        check_in, check_out = cleaned.get('check_in'), cleaned.get('check_out')
        if check_in and check_in < date.today():
            self.add_error('check_in', 'Choose today or a future date.')
        if check_in and check_out and check_out <= check_in:
            self.add_error('check_out', 'Check-out must be after check-in.')
        return cleaned
