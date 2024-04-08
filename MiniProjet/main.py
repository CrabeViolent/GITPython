from salleCinemas.salleCinema import SalleCinema
from salleCinemas.salleCinemaDAO import salleCinemaDAO
from personnes.personne import Personne
from personnes.personneDAO import ListePersonneDAO
from fileAttentes.fileAttenteDAO import fileAttenteDAO

def main():
    # Test de salleCinemaDAO
    salleCinemaDAO.reserver_place("John", "A1")

    
    salleCinemaDAO.reserver_place_speciales("Alice", "VIP1")

    
    salleCinemaDAO.afficher_places_reservee()

    
    salleCinemaDAO.nombre_places_disponibles()

    
    salleCinemaDAO.filtrer_reservations_par_personne("John")

    
    message = salleCinemaDAO.annuler_reservations("Alice")
    print("Cancellation message:", message)

    # Test de personneDAO
    personne1 = Personne("Alice", 25)
    message = ListePersonneDAO.ajouter_personne(personne1)
    print(message)

    personnes, message = ListePersonneDAO.afficher_personnes()
    if message == "success":
        print("All persons:")
        for personne in personnes:
            print(f"Nom: {personne[0]}, Age: {personne[1]}")

    search_result = ListePersonneDAO.rechercher_personne("Alice")
    if search_result:
        print(f"Person found: {search_result}")
    else:
        print("Person not found.")

    message = ListePersonneDAO.update("Alice", 30)
    print(message)

    message = ListePersonneDAO.delete("Alice")
    print(message)

    ListePersonneDAO.filtrer_personne_par_age(20, 30)

    # Test de fileAttenteDAO
    personne1 = Personne("Micheal", "non-prioritaire")
    personne2 = Personne("Johnny", "prioritaire")

    fileAttenteDAO.ajouter_personne_en_attente(personne1)
    fileAttenteDAO.ajouter_personne_en_attente_prioritaire(personne2)

    message = fileAttenteDAO.supprimer_personne_de_attente()
    print(message)


main()
    