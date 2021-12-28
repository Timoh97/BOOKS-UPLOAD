from django import forms
from .models import Movies


# Create your forms here.
class MovieForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = ('file', 'image','author',"year_published",'title')