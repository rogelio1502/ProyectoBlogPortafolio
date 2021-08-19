from django import forms
from .models import Post,Comment

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        exclude = ('author','slug',)
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titulo"   
        self.fields['content'].label = "¿Qué estas pensando?"
        self.fields['thumbnail'].label = "Agrega una imagen"   
        self.fields['thumbnail'].required = False
   



class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={
        'rows':4,
        'style':'resize:none;',
    }))
    class Meta:
        model = Comment
        fields = ('content',)
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Expresate"
