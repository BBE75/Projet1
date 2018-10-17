import settings


def delete_user(username):
    with open(settings.CSV_FILE, "r") as source:
        data = list(settings.csv.reader(source))

    with open(settings.CSV_FILE, "w", newline='') as destination:
        writer = settings.csv.writer(destination)
        for row in data:
            if row[0] != username:
                writer.writerow(row)
