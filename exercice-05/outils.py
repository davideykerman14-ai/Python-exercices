def convertir_note(texte):
    try:
        return float(texte.replace(",", "."))
    except: 
        return None
    
def moyenne(valeurs):
     return sum(valeurs) / len(valeurs)


def mention(note):
    if note >= 16:
        return ("Mention Très Bien")
    elif note >= 14:
        return("Mention Bien")
    elif note >= 12:
        return("Mention Assez Bien")
    elif note >= 10:
        return("Passable")
    else:
        return("Insuffisant")
    

