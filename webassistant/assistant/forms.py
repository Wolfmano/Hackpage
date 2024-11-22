from django import forms
from .models import Ticket, Category

class TicketForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Выберите категорию',
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full p-2 border rounded focus:outline-none focus:shadow-outline',
        })
    )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'name',
                'placeholder': 'Дайте описание в пару слов',
                'class': 'w-full p-2 border rounded focus:outline-none focus:shadow-outline',
            }),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-2 border rounded focus:outline-none focus:shadow-outline',
            }),
        }