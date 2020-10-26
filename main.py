from art import *



def create_contact(name, phone_number, is_favorite):
    contact = {
        "Noms": name,
        "phone_number": phone_number,
        "Favori": is_favorite,
              }
    return contact

carnet = {}

def add_contact(c) :
        phone_number = c["phone_number"]
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

def display_all():
    for k in carnet:
        n = carnet[k]
        print(n)

def get_contact(phone_number):
    return carnet[phone_number]



get_names()
display_all()
print(get_contact("097865434"))








