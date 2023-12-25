from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5, required=True)
    text = forms.CharField(max_length=1000, widget=forms.Textarea, required=True)
