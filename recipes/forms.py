from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title', 'description', 'ingredients', 'instructions',
            'cooking_time', 'servings', 'difficulty', 'category', 'image'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter recipe title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'placeholder': 'Brief description of the recipe'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 5,
                'placeholder': 'One ingredient per line'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 6,
                'placeholder': 'Step-by-step instructions'
            }),
            'cooking_time': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Minutes'
            }),
            'servings': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Number of servings'
            }),
            'difficulty': forms.Select(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }
