import string

def crypt(message, pas):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    resultat = ""

    for lettre in message:
        if lettre in caracteres:
            index = caracteres.index(lettre)
            nouvel_index = (index + pas) % len(caracteres)
            resultat += caracteres[nouvel_index]
        else:
            resultat += lettre

    return resultat + str(pas)
