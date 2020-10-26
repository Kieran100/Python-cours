from art import *



def create_contact(name, phone_number, is_favorite):
    contact = {
        "Noms": name,
        "Numeros": phone_number,
        "Favori": is_favorite,
              }
    return contact

carnet = {}

def add_contact(c) :
        phone_number = c["Numeros"]
        carnet[phone_number] = c

c = create_contact(name= "Kieran", phone_number="097865434" , is_favorite= True)
add_contact(c)

c = create_contact( "George", "064333234" ,  False)
add_contact(c)

def get_names():
    names = []
    for k in sorted(carnet):
        n = carnet[k]["Noms"]
        print(n)
    return names

get_names()










