class Participants:
    def __init__(self, nom_prenom="", conjoint=""):
        self.nom_prenom = nom_prenom
        self.conjoint = conjoint
    def __str__(self):
        return f"Nom : {self.nom_prenom} , " \
               f"Conjoint : {self.conjoint}"