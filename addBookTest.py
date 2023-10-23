# CLIENT SIDE

import requests
import json

headers = {
    'Content-Type': 'application/json',
}

# get all books
print("ALL BOOKS:")
response = requests.get('http://127.0.0.1:8080')
print(response.text)

# get a specific book
print('BOOK NUMBER 3:')
response = requests.get('http://127.0.0.1:8080/3')
print(response.text)

# add a new book
print('ADDING A NEW BOOK')
response = requests.post('http://127.0.0.1:8080/add-book', json.dumps({
    'name': 'Example',
    'author': 'Me',
    'pages': 9999,
    'publication_date': '1995'
}), headers)
print(response.text)

# updating a book
print("UPDATING A BOOK:") 
response = requests.put('http://127.0.0.1:8080/update-book/4', json.dumps({
    'name': 'Name Changed!',
}))
print(response.text)

# deleting a book
response = requests.delete('http://127.0.0.1:8080/delete-book/4')
print(response.text)
