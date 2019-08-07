from flask import abort, request
from flask_restful import Resource
from  vocabulary_catalogue.models.model import db, Book, Vocab, VocabSchema

vocab_schema = VocabSchema(many=True)

class VocabResource(Resource):
    def get(self, title=None, limit=None):
        if limit:
            most = vocab_schema.dump(Vocab.query.order_by(Vocab.count.desc()).limit(limit)).data
            least = vocab_schema.dump(Vocab.query.order_by(Vocab.count).limit(limit)).data
            return {"{} most frequent words used".format(limit): most, "{} least frequent words used".format(limit): least}, 200
        if title:
            book = Book.query.filter_by(title=title).one_or_none()
            if book is None:
                return {'message': 'Unable to find book'}, 404
            data = vocab_schema.dump(Vocab.query.filter_by(book_id=book.id)).data

        return data, 200
