from django import forms
from .models import Post, Profile, Relationship

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'dob', 'bio']

class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = ['status']




