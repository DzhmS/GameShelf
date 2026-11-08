from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'rating', 'comment']

        labels = {
            'rating': 'Score',
            'comment': 'Review Comment',
        }

        help_texts = {
            'rating': 'Enter a score from 1 to 100.',

        }

        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'placeholder': '1-100',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Write your review here...',
                }
            ),

        }


        error_messages = {
            'rating': {
                'required': 'Please enter a score.',
                'invalid': 'Please enter a valid number.',
            },

        }

    def clean_comment(self):
        comment = self.cleaned_data['comment'].strip()

        if comment and  len(comment) < 5:
            raise forms.ValidationError(
                'Comment must contain at least 5 characters.'
            )

        return comment

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['game'].disabled = True