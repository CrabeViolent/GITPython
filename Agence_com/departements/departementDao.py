import database as db
from departements.departement import Departement

class DepartementDao:
    connexion = db.connect_db()
    cursor = connexion.cursor()

    def __init__(self, nom, emplacement, direction):
        self.nom = nom
        self.emplacement = emplacement
        self.direction = direction
    
    # Class methods #
    @classmethod
    def create(cls, dep:Departement):
        sql = "INSERT INTO Departement(nom,emplacement,direction) VALUES(%s,%s,%s)"
        parameters = (dep.nom, dep.emplacement, dep.direction)
        try:
            DepartementDao.cursor.execute(sql, parameters)
            DepartementDao.connexion.commit()
            DepartementDao.cursor.close()
            message = f"Le département {dep.nom} a bien été ajouté !"
        except Exception as error:
            print(error)
            message = "ERREUR! ERREUR! ERREUR! ERREUR!"
        return message
    
    @classmethod
    def read_all(cls):
        sql = "SELECT * FROM departement"
        DepartementDao.cursor.execute(sql)
        departements = DepartementDao.cursor.fetchall()
        DepartementDao.cursor.close()
        for departement in departements:
            print(departement)
            print("----------------------------------------")
        
    @classmethod
    def read_one(cls,name):
        sql = "SELECT * FROM departement WHERE nom=%s"
        DepartementDao.cursor.execute(sql, (name,))
        info = DepartementDao.cursor.fetchone()
        print(info)

    @classmethod
    def delete(cls, nom):
        sql = "DELETE FROM departement WHERE nom=%s"
        DepartementDao.cursor.execute(sql, (nom,))
        DepartementDao.connexion.commit()
        DepartementDao.cursor.close()

    @classmethod  
    def get_all(cls):
        sql = "SELECT * FROM departement"
        try:
            cls.cursor.execute(sql)
            departements = cls.cursor.fetchall()
            message = "success"
        except Exception as error:
            departements = []
            message = "Erreur de récupération des données ! "
        return (message, departements)
    
    @classmethod  
    def get_all_nom(cls):
        sql = "SELECT nom FROM departement"
        try:
            cls.cursor.execute(sql)
            departements = cls.cursor.fetchall()
        except Exception as error:
            departements = []
        return (departements)

    @classmethod
    def add(cls, departement: Departement):
        sql = "INSERT INTO departement(nom, emplacement, direction) VALUES(%s,%s,%s)"
        params = (departement.nom, departement.emplacement, departement.direction)
        try:
            cls.cursor.execute(sql, params)
            cls.connexion.commit()
            message = "success"
        except Exception as error:
            message = "error"
            print(error)
        return (message)



