def notes_arrondies(notes):
    liste_notes = []
    for note in notes:
        if note <40:
            liste_notes.append(note)
        elif note >= 40 and note % 5 >= 3:
            liste_notes.append(note + (5 - note % 5))
        else:
            liste_notes.append(note)
    return liste_notes

print(notes_arrondies([73, 67, 38, 33, 46,78,90, 97,87,88]))