import logger as l
import logging


def create_contact(name, phone_number, is_favorite):
    """
    Fonction pour créer des contacts
    :param name: nom du contact
    :param phone_number: numeros de téléphone du contact
    :param is_favorite: est-il dans les favoris
    :return: contact en entier
    """
    contact = {
        "Noms": name,
        "phone_number": phone_number,
        "Favori": is_favorite,
              }
    return contact

carnet = {}

def add_contact(c) :
        """
        Fonction pour ajouter un contact
        :param c: contact du phone_number
        :return: ajout du contact
        """
        phone_number = c["phone_number"]
        carnet[phone_number] = c
        l.log_add("Contact ajouté")

try:
    c = create_contact(name="Kieran", phone_number="097865434", is_favorite=True)
    add_contact(c)
    c = create_contact("albert")
    add_contact(c)
    c = create_contact("George", "064333234", False)
    add_contact(c)
except TypeError as e:
    print("erreur il manque des paramètres")


def get_names():
    """
    Fonction pour sortir la liste de noms
    :return: les noms dans l'odre alphabetic
    """
    names = []
    for k in sorted(carnet):
        n = carnet[k]["Noms"]
        print(n)
    return names

def display_all():
    """
    Fonction pour afficher les contacts
    :return: tous les contacts
    """
    for k in carnet:
        n = carnet[k]
        print(n)
    logging.basicConfig(format =('%(asctime)s :: %(message)s'))
    l.log_add("affichage des contacts")

def get_contact(phone_number):
        """
        Fonction trouver un contact
        :param phone_number: la clé pour trouver le contact
        :return: le contact
        """
        l.log_add(f"Le numeros est attribuer a {carnet[phone_number]}")
        return carnet[phone_number]
