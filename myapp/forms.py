from django import forms
from .models import Produit, More_Culture, SuggestModel, ContactModel

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'image']
    
class MoreCulture(forms.ModelForm):
    class Meta:
        model = More_Culture
        fields = ['name','fonction','description','image_pic']

class SuggestForm(forms.ModelForm):
    class Meta:
        model = SuggestModel
        fields = ['name','email','subject','message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['first_name', 'email_address', 'subject', 'write_message']