import random

from django.shortcuts import render
from models import Participants

def control_self_and_conjoint(participant, secret_santa):
    if participant.nom_prenom == secret_santa or participant.conjoint == secret_santa:
        return False
    else:
        return True

def secret_santa(list_of_participants):
    """
    Effectue un tirage au sort par paire pour un Secret Santa.
    Args:
      participants: Une liste de participants.
    """
    list_copy = list(list_of_participants)
    list_return = []

    for participant in list_of_participants:
        secret = list_copy[random.randint(0, len(list_copy) - 1)]
        # Tant que la fonction de control est fausse fait recommencer le tirage afin de ne pas avoir le conjoint ni soit meme.
        while control_self_and_conjoint(participant, secret.nom_prenom) is False:
            secret = list_copy[random.randint(0, len(list_copy) - 1)]
        list_copy.remove(secret)
        list_return.append(f"{participant.nom_prenom} doit offrir un cadeau à {secret.nom_prenom}")
    return list_return
def main_view(request):
    list_participants_Cadoret = [
        Participants("Antho", "Anais"),
        Participants("Anais", "Antho"),
        Participants("Léo", "Méline"),
        Participants("Méline", "Léo"),
        Participants("Roselyne", "Jean-Mi"),
        Participants("Jean-Mi", "Roselyne"),
        Participants("Domi", ""),
        Participants("Audrey", "Fabien"),
        Participants("Fabien", "Audrey"),
    ]

    list_participants_Cornilleau = [
        Participants("Antho", "Anais"),
        Participants("Anais", "Antho"),
        Participants("Laurent", "Maud"),
        Participants("Maud", "Laurent"),
        Participants("Angélique", "Johnny"),
        Participants("Johnny", "Angélique"),
        Participants("Kelhen", ""),
    ]

    return render(request, 'base.html', {'secrets': secret_santa(list_participants_Cadoret)} )
