from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'body')
        
        
        
        
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control', 'id':'exampleFormControlInput1', 'placeholder':'Title'}),

            'body': forms.Textarea(attrs={'class':'form-control', 'id':'exampleFormControlTextarea1'})   
        }



