class FileAttente:
    def __init__(self):
        self.__file_attente = []
        self.__file_attente_prioritaire = []

        # Getters and setters
    @property
    def file_attente(self):
        return self.__file_attente
    @file_attente.setter
    def file_attente(self, newfileAttente):
        self.__file_attente = newfileAttente
    
    @property
    def file_attente_prioritaire(self):
        return self.file_attente_prioritaire
    @file_attente_prioritaire.setter
    def file_attente_prioritaire(self, newfileAttente):
        self.__file_attente_prioritaire = newfileAttente

    