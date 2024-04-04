class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    # Getters and setters
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, value):
        self.__nom = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value
    


class ListePersonne:
    def __init__(self):
        self.__personne_list = []

    # Getters and setters
    @property
    def personne_list(self):
        return self.__personne_list

    @personne_list.setter
    def personne_list(self, new_list):
        self.__personne_list = new_list
    