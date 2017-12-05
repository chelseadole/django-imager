"""Forms outline for editing a Profile."""

from django import forms
from imager_profile.models import Profile


class EditProfileForm(forms.ModelForm):
    """Edit Profile."""

    def __init__(self, *args, **kwargs):
        """Initializing Profile Form."""
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['Username'] = forms.CharField(initial=self.instance.user.username)
        self.fields['Password'] = forms.CharField(initial=self.instance.user.password)
        self.fields['Email'] = forms.EmailField(initial=self.instance.user.email)
        del self.fields['user']

    class Meta:
        """User metadata."""

        model = Profile
        exclude = []
