from django import forms

from .models import Platform


class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter name'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Enter description'}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                'Platform name must contain at least 2 characters.'
            )

        return name