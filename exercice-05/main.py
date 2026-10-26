from outils import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes = []
 
for texte in notes_brutes:
    note = convertir_note(texte)
    
    if note is not None:
        notes.append(note)

notes_ignorees = len(notes_brutes) - len(notes)

print("Notes ignorées :", notes_ignorees)

print("Moyenne :", round(moyenne(notes), 2))

print("Mention :", mention(moyenne(notes)))