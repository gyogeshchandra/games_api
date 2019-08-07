import string

from flask import abort, request
from flask_restful import Resource
from  vocabulary_catalogue.models.model import db, Book, BookSchema, Vocab

book_schema = BookSchema(strict=True)
books_schema = BookSchema(many=True)

class BookResource(Resource):
    def get(self, id=None):
        if id == None:
            data = books_schema.dump(Book.query.all()).data
        else:
            data = books_schema.dump(Book.query.filter_by(id=id)).data

        return data, 200

    def post(self):
        json_data = request.get_json()
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        data, errors = book_schema.load(json_data)
        if errors:
            return errors, 422
        char_limit = data.get('char_limit')
        book = Book.query.filter_by(title=data['title']).first()
        if book:
            return {'message': 'Book already exists'}, 400
        book = Book(
            title=json_data['title'],
            author=json_data['author'],
            )
        db.session.add(book)
        db.session.flush()

        if data.get('abstract'):
            for word in data['abstract'].split():
                word = word.translate(str.maketrans('', '', string.punctuation))
                if char_limit and len(word) <= char_limit:
                    continue
                vocab = Vocab.query.filter_by(word=word).one_or_none()
                if vocab is None:
                    data = Vocab(count=0, word=word, book_id=book.id)
                    db.session.add(data)
                else:
                    vocab.count += 1

        db.session.commit()
        result = book_schema.dump(book).data

        return result, 201

    def put(self, id=None):
        if not id:
            abort(405)
        json_data = request.get_json()
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        data, errors = book_schema.load(json_data)
        if errors:
            return errors, 422
        book = Book.query.filter_by(id=id).first()
        if not book:
            return {'message': 'Unable to find book'}, 400

        if data.get('author'):
            book.author = data['author']
        if data.get('title'):
            book.title = data['title']

        db.session.commit()
        result = book_schema.dump(book).data
        return result, 204

    def delete(self, id=None):
        if id is None:
            abort(405)
        book = Book.query.filter_by(id=id).one_or_none()
        if book is None:
            return {'message': 'Unable to find book'}, 404
        book.delete()
        db.session.commit()

        return None, 204	
