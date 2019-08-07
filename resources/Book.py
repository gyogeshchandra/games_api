from flask import abort, request
from flask_restful import Resource
from Model import db, Book, BookSchema

book_schema = BookSchema(strict=True)
books_schema = BookSchema(many=True)

class BookResource(Resource):
    def get(self, id=None):
        if id == None:
            data = book_schema.dump(Book.query.all())
        else:
            data = books_schema.dump(Book.query.filter_by(id=id))
        return {'status': 'success', 'data': data}, 200

    def post(self):
        json_data = request.get_json()
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = book_schema.load(json_data)
        if errors:
            return errors, 422
        book = Book.query.filter_by(title=data['title']).first()
        if book:
            return {'message': 'Book already exists'}, 400
        book = Book(
            title=json_data['title'],
            author=json_data['author'],
            )

        db.session.add(book)
        db.session.commit()

        result = book_schema.dump(book).data

        return {'data': result }, 201

    def delete(self, id=None):
        if id is None:
            abort(405)

        book = Book.query.filter_by(id=id).delete()
        db.session.commit()

        return None, 204	
