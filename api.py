from flask import Flask, jsonify, request
from library_management import get_books, add_new_book, get_a_book, update_book_data, delete_book_record
import json

app = Flask(__name__)

@app.route('/')
def all_thoughts():
    return jsonify(get_books()), 200

@app.route('/<id>', methods=["GET"])
def get_book(id):
    return jsonify(get_a_book(id)), 200

@app.route('/add-book', methods=['POST'])
def add_book():
    new_book = json.loads(request.data)
    add_new_book(new_book)
    return get_books(), 201

@app.route('/update-book/<id>', methods=["PUT"])
def update_book(id):
    print('here')
    print(request)
    print(request.data)
    new_data = json.loads(request.data)
    update_book_data(id, new_data)
    return get_a_book(id)

@app.route('/delete-book/<id>', methods=["DELETE"])
def delete_message(id):
    delete_book_record(id)
    return get_books(), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)
