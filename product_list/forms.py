from django import forms
from django.core.exceptions import ValidationError
from product_list.models import ListItem

class ListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ["name","status"]
