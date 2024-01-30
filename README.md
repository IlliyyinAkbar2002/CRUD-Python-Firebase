# Firebase CRUD Operations in Python

This project demonstrates how to perform Create, Read, Update, and Delete (CRUD) operations in Python using Firebase as the backend database.

## Project Structure

The project consists of a single Python script, `app.py`, which contains the following functions:

- `create()`: This function prompts the user for a name and age, then creates a new document in the Firebase collection with these details.

- `read()`: This function retrieves all documents from the Firebase collection and prints their details.

- `update()`: This function prompts the user for a name and age, then updates the corresponding document in the Firebase collection with the new details.

- `delete()`: This function prompts the user for a name, then deletes the corresponding document from the Firebase collection.

- `main()`: This function provides a simple command-line interface for the user to select which operation they want to perform.

## Setup

To run this project, you need to have a Firebase project set up and replace the `cred_path` variable in `app.py` with the path to your Firebase project's service account key JSON file.

## Usage

Run the `app.py` script and follow the prompts to perform CRUD operations on your Firebase collection.