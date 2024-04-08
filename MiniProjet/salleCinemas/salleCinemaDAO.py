from salleCinemas.salleCinema import SalleCinema
import database as db

class salleCinemaDAO:
    connexion = db.connexion()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    # # # CRUD classmethods # # # 

    # RÉSERVER PLACES ORDINAIRES
    @classmethod
    def reserver_place(cls, nom, place):
        # # # Verification du nombre de places disponibles     
        sql = "SELECT * FROM reservations WHERE type='ordinaire'"
        salleCinemaDAO.cursor.execute(sql)
        liste = salleCinemaDAO.cursor.fetchall()
        nb_places = len(liste)


        if nb_places < SalleCinema().capacite:
            sql = "INSERT INTO reservations (nom,place,type) VALUES(%s,%s,%s)"
            salleCinemaDAO.cursor.execute(sql, (nom,place,"ordinaire"))
            print("\n|=-= =-= =-= S U C C È S =-= =-= =-= =-= =-= =-= =-= =-= =-=|")
            print(f"| La place {place} a bien été réservée pour {nom}          |")
            print("|=-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-=|\n")
        else:
            print("\n=-=-=-=-=-=-= É C H E C =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|  Zut.. Il n'y a plus de places disponibles . . .        |")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        
        salleCinemaDAO.connexion.commit()
        salleCinemaDAO.cursor.close()

    # RÉSERVER PLACES SPÉCIALES
    @classmethod
    def reserver_place_speciales(cls, nom, place):
        # # # Verification du nombre de places disponibles     
        sql = "SELECT * FROM reservations WHERE type='special'"
        salleCinemaDAO.cursor.execute(sql)
        liste = salleCinemaDAO.cursor.fetchall()
        nb_places = len(liste)

        if nb_places < SalleCinema().capacite_speciale:
            sql = "INSERT INTO reservations (nom,place,type) VALUES(%s,%s,%s)"
            salleCinemaDAO.cursor.execute(sql, (nom,place,"special"))
            print("\n|=-= =-= =-= S U C C È S =-= =-= =-= =-= =-= =-= =-= =-= =-=|")
            print(f"| La place spéciale {place} a bien été réservée pour {nom}  |")
            print("|=-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-= =-=|\n")
        else:
            print("\n|=-=-=-=-=-=-= É C H E C =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
            print("|  Zut.. Il n'y a plus de places spéciales disponibles ...  |")
            print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|\n")
        
        salleCinemaDAO.connexion.commit()
        salleCinemaDAO.cursor.close()

    # AFFICHER PLACES RESERVÉES
    @classmethod
    def afficher_places_reservee(cls):
        sql = "SELECT * FROM reservations"
        salleCinemaDAO.cursor.execute(sql)
        reservations = salleCinemaDAO.cursor.fetchall()
        for reservation in reservations:
            print(f"\n Nom : {reservation[0]} || Place : {reservation[1]} || Type : {reservation[2]}")
            print("=--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---=")
        salleCinemaDAO.cursor.close()

    # AFFICHER PLACES DISPONIBLES
    @classmethod
    def nombre_places_disponibles(cls):
        sql = "SELECT * FROM reservations WHERE type='ordinaire'"
        salleCinemaDAO.cursor.execute(sql)
        nb_places = salleCinemaDAO.cursor.fetchall()

        sql = "SELECT * FROM reservations WHERE type='special'"
        salleCinemaDAO.cursor.execute(sql)
        nb_places_speciales = salleCinemaDAO.cursor.fetchall()

        print("\n|=-= =-= =-= =-= =- PLACES DISPONIBLES -= =-= =-= =-= =-=|")
        print(f"       Places 'ordinaires' disponibles  :  {SalleCinema.capacite - nb_places}")
        print(f"       Places 'speciales' disponibles   :  {SalleCinema.capacite_speciale - nb_places_speciales}\n")
        salleCinemaDAO.cursor.close()

    # FILTRER RÉSERVATIONS PAR PERSONNES
    @classmethod
    def filtrer_reservations_par_personne(cls, nom):

        sql = "SELECT * FROM reservations WHERE nom=%s"
        salleCinemaDAO.cursor.execute(sql, (nom))
        all_reservations = salleCinemaDAO.cursor.fetchall()
        if all_reservations:
            print(f"\n|=-=-=    TOUT LES RÉSERVATIONS DE :  {nom}  =-=-=|")
            for reservation in all_reservations:
                print(f"   Nom :   {reservation[0]}  |   Place :   {reservation[1]}  |   Type :   {reservation[2]} ")
                print("|---                                                                                 ---|")
        else:
            print("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
            print("|=|   Le nom indiqué n'est pas dans notre liste de réservations  |=|")
            print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|\n")
        salleCinemaDAO.cursor.close()

    # ANNULER RÉSERVATIONS
    @classmethod
    def annuler_reservations(cls, nom):
        sql = "SELECT * FROM reservations WHERE nom=%s"
        salleCinemaDAO.cursor.execute(sql, (nom))
        all_reservations = salleCinemaDAO.cursor.fetchall()
        if all_reservations:
            print(f"\n|=-=-=    RÉSERVATIONS SUPPRIMÉES :  =-=-=|")
            for reservation in all_reservations:
                print(f"   Nom :   {reservation[0]}  |   Place :   {reservation[1]}  |   Type :   {reservation[2]} ")
                print("|---                                                                                 ---|")
        else:
            print("\n|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
            print("|=|   Le nom indiqué n'est pas dans notre liste de réservations  |=|")
            print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|\n")

        try:
            sql = "DELETE FROM reservations WHERE nom=%s"
            salleCinemaDAO.cursor.execute(sql, (nom,))
            salleCinemaDAO.connexion.commit()
            message = "SUCCÈS"
        except Exception as error:
            message = "ÉCHEC!"
        salleCinemaDAO.cursor.close()
        return message



