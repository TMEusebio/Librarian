# Librarian - Personal Book Cataloging Assistant

## Overview
Librarian is a simple Python-based tool designed to help you manage your personal book collection. By entering an ISBN, the program fetches book details from Open Library and allows you to add additional information manually. The data is then stored in an Excel spreadsheet for easy organization and future reference.

## Features
- 📖 Fetches book details automatically using Open Library API
- ✍️ Allows manual entry of additional book details (e.g., language, genre, translator)
- 💾 Saves all data in an organized Excel file (`library.xlsx`)
- 🔍 Provides an interactive way to confirm and edit book information

## Installation
To use Librarian, you need to install the required dependencies. Run the following command in your terminal:
```sh
pip install requests pandas openpyxl
```

## Usage
1. Run the script:
   ```sh
   python librarian.py
   ```
2. Enter the **ISBN** of the book when prompted.
3. Review the automatically fetched book details.
4. If necessary, correct any information.
5. Enter additional book details manually (e.g., **original language, genre, translator, nationality**).
6. Confirm the final details.
7. The book is saved in `library.xlsx`.

## Example
```
---------------------------------------------------------------
--------------------Welcome to the C&T Library!-----------------
---------------------------------------------------------------
Let's add a new book!
Enter ISBN: 9780140449136

-----------------------New Book-------------------------------
 1) ISBN                   :        9780140449136
 2) Title                  :         "Dubliners"
 3) Author                 :       James Joyce
 4) Publisher              :      Penguin Classics
 5) Year of Publication    :            1992
---------------------------------------------------------------
Are the book data correct? (y/n): y

Please enter the following fields manually:
Year of First Edition: 1914
Original language: English
Text language: English
Genre: Fiction
Nationality: Irish
Obs.: Short story collection
Read by (C/T/CT): CT
---------------------------------------------------------------
Congratulations! A new book was added to the library!
---------------------------------------------------------------
```

## File Format
Each book entry is stored in an Excel file (`library.xlsx`) with the following columns:
- ISBN
- Title
- Author
- Publisher
- Year of Publication
- Year of First Edition
- Original language
- Text language
- Translator
- Genre
- Nationality
- Obs.
- Read


## Contributions
Feel free to fork this repository, submit pull requests, or suggest improvements!


