import phonebook as P
import logger as l
import logging
#import utils  #Import du module
#from utils import say_hello

P.get_names()
P.display_all()
try:
    print(P.get_contact("064333234"))
except KeyError as e:
    print(f'erreur : {e}')

l.dump_log()








