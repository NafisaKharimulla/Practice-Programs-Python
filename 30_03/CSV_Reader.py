import csv

def read_csv(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            print("Columns:", header)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("File not found")

file = input("Enter CSV file name: ")
read_csv(file)