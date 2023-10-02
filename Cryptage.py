import string

def crypt(message):
    caracteres = string.ascii_letters + string.digits + string.punctuation + " "
    resultat = ""

    for char in message:
        if char in caracteres:
            index = caracteres.index(char)
            resultat += caracteres[(index + 1) % len(caracteres)]
        else:
            resultat += char

    return resultat
