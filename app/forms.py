from .models import Profile, Links
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'description', 'twitter', 'github', 'linkedin', 'template']


class LinksForm(ModelForm):
    class Meta:
        model = Links
        fields = ['Description', 'link']