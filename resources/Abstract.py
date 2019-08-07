from flask import abort, request
from flask_restful import Resource
from Model import db, Book, Vocab, VocabSchema, BookAbstract, BookAbstractSchema

abstract_schema = BookAbstractSchema()

class BookAbstractResource(Resource):
    def post(self, title=None):
        if title is None:
            abort(405)
        else:
            book = Book.query.filter_by(title=title).one_or_none()
        if book is None:
            return {'status': 'failed', 'message': 'Unable to find book'}, 404
        json_data = request.get_json()
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = abstract_schema.load(json_data)
        if errors:
            return errors, 422
        # book_json = Book.query.filter_by(title=data['book_id']).first()
        # if book_json.id != book.id:
        #     return {'message': 'Inconsistent data'}, 400
        book_abstract = BookAbstract(
            abstract=json_data['abstract'],
            book_id=book.id,
            )
        db.session.add(book_abstract)

        words = json_data['abstract'].split()
        for word in words:
            vocab = Vocab.query.filter_by(word=word).one_or_none()
            if vocab is None:
                data = Vocab(count=0, word=word, book_id=book.id)
                db.session.add(data)
            else:
                vocab.count += 1
        db.session.commit()

        result = abstract_schema.dump(book_abstract).data

        return {'data': result }, 201
