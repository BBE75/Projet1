import settings


def update(username):
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]


        #     # consultation du csv
        #     elif choix == 4:
        #         cs = open("C:/Users/phili/Desktop/user.csv", "r+")
        #         ligne = csv.reader(cs)
        #         for row in ligne:
        #             # affiche toutes les lignes
        #             print(', '.join(row))
        #     break
        #
        #     # quitte
        #     if choix == 0:
        #     break