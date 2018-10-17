import settings


def listuser():
    print('*****LIST OF ALL KNOWN USER*****')
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        skipheader = next(reader)
        for row in reader:
            data[row[0]] = row[1:]
        for index, item in enumerate(data):
            row = str(index+1)+'.'+item
            print(row)
