from flask import Blueprint, jsonify
from flask_restful import Api
from resources.Hello import Hello
from resources.Book import BookResource
from resources.Vocab import VocabResource
from resources.Abstract import BookAbstractResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route

@api_bp.route("/", methods = ["GET", "POST"])
def index():
    return jsonify("Welcome to Vocabulary Builder!")

api.add_resource(
    BookResource,
    '/books',
    '/book/id/<int:id>'
)

api.add_resource(
   VocabResource,
   '/book/<string:title>/vocab'
)

api.add_resource(
   BookAbstractResource,
   '/book/<string:title>/abstract'
)
