import phonebook as P
import logger as l
import sys
#import utils  #Import du module
#from utils import say_hello

P.get_names()
P.display_all()
try:
    print(P.get_contact("064333234"))
except KeyError as e:
    print(f'erreur : {e}')

try:
    args = sys.argv
    arg1 = args[1]
    arg2 = args[2]
    arg3 = args[3]
except IndexError as e:
    print("erreur")

if arg1 == "-log":
     l.dump_log()


#elif
try:
   # if arg2 == "-display" and arg3 == "097865434":
    if arg2 == "-display":
     print(P.get_contact(arg3))
    # print(P.get_contact("097865434"))
except Exception as e:
    print("Mauvais numeros")






