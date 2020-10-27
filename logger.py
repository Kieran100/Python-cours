import logging


#formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

def log_add(message):
    with open('phonebook.log', 'a') as f:
        #     logging.basicConfig(format='%(asctime)s')
              f.write( message + "\n")


def dump_log():
    with open('phonebook.log', 'r') as f:
        line = f.readline()
        print(line)
        while line:
          line = f.readline()

