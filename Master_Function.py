


import random
import string

def envès_mo(mot):
    return mot[::-1]
mo_envès = envès_mo("Bonjour")
print(mo_envès)  # Pral afiche "ruojnuoB"




def kòd_aleyatwa(n):
    kòd = ''.join(random.choice(string.ascii_letters) for _ in range(n))
    return kòd


def kòd_aleyatwa_alafanimerik(n):
    kòd = ''.join(random.sample(string.ascii_letters + string.digits, n))
    return kòd



def jenere_slug(chenn):
    slug = ''.join(c if c.isalnum() or c == '-' else '' for c in chenn)
    return slug



def separe_let_ak_vigel(mot):
    mot_separe = '-'.join(mot)
    return mot_separe

def kripte_alfabet(mot):
    kripte = '-'.join(str(ord(c) - ord('A')) for c in mot.upper())
    return kripte



def retounen_dyo_paramet(paramèt1, paramèt2):
    return (paramèt1, paramèt2)


def inisyal_non(non):
    inisyal = ''.join(word[0] for word in non.split('-'))
    return inisyal

