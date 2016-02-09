from django.forms import ModelForm
from django.forms.widgets import Textarea, TextInput
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'context', 'author']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['context'].widget = Textarea(attrs={
            'class': 'form-control',
        })
        self.fields['title'].widget = TextInput(attrs={
            'class': 'form-control',
        })
        self.fields['author'].widget = TextInput(attrs={
            'class': 'form-control',
        })





