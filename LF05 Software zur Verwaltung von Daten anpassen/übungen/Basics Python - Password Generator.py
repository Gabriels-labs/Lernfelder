import string
import secrets

#4 Gruppen:
gross = string.ascii_uppercase
klein = string.ascii_lowercase
zahlen = string.digits
sonder = "!@#$%^&*()_+-=[]{};:,.?"

#zusammenfassen:
alle = gross + klein + zahlen + sonder

#mind. 1 Symbol aus jeder Gruppe:
password = [
    secrets.choice(gross),
    secrets.choice(klein),
    secrets.choice(zahlen),
    secrets.choice(sonder)
]

#damit 16 Symbole sind:
while len(password) < 16:
    password.append(secrets.choice(alle))

#mischen:
secrets.SystemRandom().shuffle(password)

#in String umwandeln:
fertiges_passwort = "".join(password)

#Ausgabe:
print("Dein Password:", fertiges_passwort)
