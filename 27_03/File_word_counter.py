def count_words(file_name):
    try:
        with open(file_name, "r") as f:
            text = f.read()
            words = text.split()
            print("Total words:", len(words))
    except FileNotFoundError:
        print("File not found!")

file = input("Enter file name: ")
count_words(file)