# Librarian - Personal Book Cataloging Assistant

import requests     # Used to fetch book details from the Open Library API.
import pandas as pd # Helps in managing and storing book data in an Excel file.
import os           # Used to check if the Excel file already exists.

# Function to get book details from openlibrary.com.
# Store data in a dictionary.
def get_book_details(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
    response = requests.get(url)
    data = response.json()

    if f"ISBN:{isbn}" not in data:
        print("Book not found!")
        return None

    book = data[f"ISBN:{isbn}"]
    title = book.get("title", "Unknown Title")
    authors = ", ".join([author["name"] for author in book.get("authors", [])])
    publishers = ", ".join([pub["name"] for pub in book.get("publishers", [])])
    publish_date = book.get("publish_date", "Unknown Year")

    return {
        "ISBN": isbn,
        "Title": title,
        "Author": authors,
        "Publisher": publishers,
        "Year of Publication": publish_date
    }

# Save the new data entry in an Excel file.
def save_to_excel(book_data, filename="library.xlsx"):
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        # The order of the columns is set here.
        df = pd.DataFrame(columns=["ISBN", "Title", "Author", "Publisher", "Year of Publication", "Year of First Edition", "Original language", "Text language", "Translator", "Genre", "Nationality", "Obs.", "Read" ])

    df = pd.concat([df, pd.DataFrame([book_data])], ignore_index=True)
    df.to_excel(filename, index=False)
    print("-----------------------------------------------------")
    print(f"Book added: {book_data['Title']}")
    #print("-------------------------------------------------")

# Run the program
if __name__ == "__main__":
    print()
    print("--------------------------------------------------------------------")
    print("--------------------Hello! I am the Librarian!----------------------")
    print("--------------------------------------------------------------------")
    print("Let's add a new book!")
    isbn = input("Enter ISBN: ")  # Asks the user to enter the ISBN of a new book.
    book = get_book_details(isbn)
    action = True
    while action == True:
        print() # Print the details of the new book.
        print("-----------------------New Book--------------------")
        #print()
        i = 1
        for key, value in book.items():
            print(f"{i}) {key:<22} : {value:>22}")
            i += 1
        #print()
        print("---------------------------------------------------")
        confirmation = input("Confirm book details (y/n): ") # Asks for confirmation. If not ok, user makes the necessary corrections.
        while True:
            if confirmation == "y":
                action = False
                break
            elif confirmation == "n":
                field = int(input("Which field do you want to correct?: "))
                keys_list = list(book.keys())
                if 0 < field <= len(keys_list):
                    book.update({keys_list[field]: input(f"{keys_list[field]}: ")})
                    break
                else:
                    print("Choose a valid number!")
    print("-------------------------------------------------")
    # Asks the user to enter manually some additional data.
    print("Please enter the following fields manually:")
    book.update({"Year of First Edition": input("Year of First Edition: ")})
    book.update({"Original language" : input("Original language: ")})
    book.update({"Text language": input("Text language: ")})
    if not book.get("Original language") == book.get("Text language"):
        book.update({"Translator": input("Translator: ")})
    book.update({"Genre": input("Genre: ")})
    book.update({"Nationality": input("Nationality: ")})
    book.update({"Obs.": input("Obs.: ")})
    book.update({"Read": input("Read by: ")})

    # # Print all the details of the new book.
    action2 = True
    while action2 == True:
        print("-----------------------New Book---------------------")
        #print()
        i = 1
        for key, value in book.items():
            if i < 10:
                print(f" {i}) {key:<22} : {value:>22}")
                i += 1
            else:
                print(f"{i}) {key:<22} : {value:>22}")
                i += 1
        #print()
        print("----------------------------------------------------")
        confirmation = input("Confirm book details (y/n): ")
        while True:
            if confirmation == "y":
                save_to_excel(book)
                action2 = False
                break
            elif confirmation == "n":
                field = int(input("Which field do you want to correct?: "))
                keys_list = list(book.keys()) # Makes a list of the dictionary keys.
                if 0 < field <= len(keys_list):
                    book.update({keys_list[field]: input(f"{keys_list[field]}: ")})
                    break
                else:
                    print("Choose a valid number!")
    #print()
    #print("-----------------------------------------------------")
    print("Congratulations! A new book was added to the library!")
    print("-----------------------------------------------------")



