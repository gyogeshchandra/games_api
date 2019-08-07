from flask import Blueprint, jsonify
from flask_restful import Api
from  vocabulary_catalogue.resources.Book import BookResource
from  vocabulary_catalogue.resources.Vocab import VocabResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route

@api_bp.route("/", methods = ["GET", "POST"])
def index():
    return jsonify("Welcome to Vocabulary Catalogue!")

api.add_resource(
    BookResource,
    '/book',
    '/book/id/<int:id>'
)

api.add_resource(
   VocabResource,
   '/book/<string:title>/vocab',
   '/vocab/stats/<int:limit>'
)
