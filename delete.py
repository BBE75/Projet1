# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

import settings


# La fonction permet de supprimer une ligne du fichier CSV en réécrivant tous le fichier CSV sans la ligne désiré
def delete_user(username):
    # On lit le fichier CSV ligne à ligne
    with open(settings.CSV_FILE, "r") as source:
        data = list(settings.csv.reader(source))
    # Et on réecrit les lignes sauf si le premier champs contient le nom de compte qu'on souhaite supprimer
    with open(settings.CSV_FILE, "w", newline='') as destination:
        writer = settings.csv.writer(destination)
        for row in data:
            if row[0] != username:
                writer.writerow(row)
