from django import forms
from hip.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

        labels = {
            'image': '프로필 사진',
        }