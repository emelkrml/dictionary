from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserProfile(models.Model):
        # This field is required.
        user = models.OneToOneField(User)
        password = models.CharField(max_length=25)

        def __unicode__(self):
                return self.user.username


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
