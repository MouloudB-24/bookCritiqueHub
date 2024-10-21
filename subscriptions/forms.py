from django import forms


class FollowUserForm(forms.Form):
    username = forms.CharField(max_length=150, label="Nom d'utilisateur")
