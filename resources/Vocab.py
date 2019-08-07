from flask import abort, request
from flask_restful import Resource
from Model import db, Book, Vocab, VocabSchema

vocab_schema = VocabSchema(many=True)

class VocabResource(Resource):
    def get(self, title=None):
        if title is None:
            abort(405)
        else:
            book = Book.query.filter_by(title=title).one_or_none()
            if book is None:
                return {'status': 'failed', 'message': 'Unable to find book'}, 404
            data = vocab_schema.dump(Vocab.query.filter_by(book_id=book.id))
        return {'data': data}, 200
