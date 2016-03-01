from django import forms
from .models import Parent, Enfant

class ParentFormulaire(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ('',)


class EnfantFormulaire(forms.ModelForm):
    class Meta:
        model = Enfant
        fields = ('Nom_de_compte', 'Prenom', 'Nom','parent')
        cocher = forms.BooleanField(help_text="Cochez svp.", required=True)

