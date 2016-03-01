from django.http import Http404
from django.shortcuts import render,redirect
from basededonnee.forms import ParentFormulaire,EnfantFormulaire
from basededonnee.models import Parent
from datetime import datetime

#from basededonnee.models import Article

def accueil(request):
    return render(request, 'basededonnee/accueil.html',locals())


def inscription(request):
    if request.method =='POST':
        form = ParentFormulaire(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.now()
            post.save()
            return redirect('http://127.0.0.1:8000/home/')
    else:
        form=ParentFormulaire()
    return render(request, 'basededonnee/inscription.html', {'form': form})

def ajoutEnfant(request):
    if request.method == 'POST':
        form = EnfantFormulaire(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.now()
            post.save()
            return redirect('http://127.0.0.1:8000/home/')
    else:
        form=EnfantFormulaire()
    return render(request, 'basededonnee/ajoutEnfant.html', {'form': form})
#def inscription(request):
 #   if request.method == 'POST':
  #      form = ParentFormulaire(request.POST)
   #     if(form.is_valid()):
    #        nom_de_compte = form.cleaned_data['nom_de_compte']
     #       Prenom = form.cleaned_data['Prenom']
      #      Nom = form.cleaned_data['Nom']
       #     envoi = True
       #     cocher = form.cleaned_date['cocher']
       # else:
       #     form = ParentFormulaire()
       # return render(request,'basededonnee/inscription.html',locals())
