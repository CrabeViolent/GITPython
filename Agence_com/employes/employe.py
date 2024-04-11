
class Employe:

    def __init__(self, nom, prenom, matricule, fonction, departement):
        self.__nom = nom
        self.__prenom = prenom
        self.__matricule = matricule
        self.__fonction = fonction
        self.__departement = departement

    # Getters and setters #
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nouveau_nom):
        self.__nom = nouveau_nom
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,nouveau_prenom):
        self.__prenom = nouveau_prenom
    @property
    def matricule(self):
        return self.__matricule
    @matricule.setter
    def matricule(self, nouveau_matricule):
        self.__matricule = nouveau_matricule
    @property
    def fonction(self):
        return self.__fonction
    @fonction.setter
    def fonction(self,nouveau_fonction):
        self.__fonction = nouveau_fonction
    @property
    def departement(self):
        return self.__departement
    @departement.setter
    def departement(self, nouveau_departement):
        self.__departement = nouveau_departement



