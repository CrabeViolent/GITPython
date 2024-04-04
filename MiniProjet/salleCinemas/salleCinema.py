class SalleCinema:
    def __init__(self):
        self.__capacite = 190
        self.__capacite_speciale = 10
        self.__places_reserves = []
        self.__places_speciales = []

    # Getters and Setters
    @property
    def capacite(self):
        return self.__capacite
    @capacite.setter
    def capacite(self, value):
        self.__capacite = value
    @property
    def capacite_speciale(self):
        return self.__capacite_speciale
    @capacite_speciale.setter
    def capacite_speciale(self, value):
        self.__capacite_speciale = value
    @property
    def places_reserves(self):
        return self.__places_reserves
    @places_reserves.setter
    def places_reserves(self, value):
        self.__places_reserves = value
    @property
    def places_speciales(self):
        return self.__places_speciales
    @places_speciales.setter
    def places_speciales(self, value):
        self.__places_speciales = value



