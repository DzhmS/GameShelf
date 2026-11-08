from django import forms

from .models import Game, Genre


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'description', 'release_date', 'developer', 'publisher', 'genres', 'platforms', 'image')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter title'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Enter description'}
            ),
            'release_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'developer': forms.TextInput(
                attrs={'placeholder': 'Enter developer'}
            ),
            'publisher': forms.TextInput(
                attrs={'placeholder': 'Enter publisher'}
            ),
            'genres': forms.CheckboxSelectMultiple(),
            'platforms': forms.CheckboxSelectMultiple(),
            'image' : forms.FileInput(),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 2:
            raise forms.ValidationError(
                'Game title must contain at least 2 characters.'
            )

        return title


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
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
                'Genre name must contain at least 2 characters.'
            )

        return name