from django import forms
from .models import Post

class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('title','tokuten','content','name','img','tell','email','url')

#class RealForm(forms.Form):
    #shop_name = forms.CharField(
       # label='名前',
        #max_length=20,
        #required=True,
        #widget=forms.TextInput()
        #)
           
  
