# from django import forms
# from .models import Post
#
#
# class CRUDforms(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'title'
#     }))
#     description = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control', 'placeholder': 'title'
#     }))
#     post_type = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'title'
#     }))
#     image = forms.ImageField()
#
#
# class Meta:
#     model = Post
#     fields = ['title', 'description', 'post_type', 'image']
